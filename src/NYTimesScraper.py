"""Gets the Daily Crossword from the New York Times website.

This script generates a CrosswordBoard object from the New York Times
website.
"""

import requests
from CrosswordBoard import CrosswordBoard as Board
from datetime import date


class NYTimesScraper(object):
    """Scrapes the New York Times website for the Daily Crossword."""

    def __init__(self) -> None:
        """Initialize the NYTimesScraper."""
        self._session = requests.Session()
        self.__init_session()
        self.__board_info_endpoint = {
            # TODO: could expand this to include switch at 10pm and other dates.
            'mini': 'https://www.nytimes.com/svc/crosswords/v6/puzzle/mini/{}.json',
            'daily': 'https://www.nytimes.com/svc/crosswords/v6/puzzle/daily/{}.json'
        }

    def __init_session(self) -> None:
        """Initialize the session."""
        self._session.headers.update({'User-Agent': 'Mozilla/5.0'})
        self._session.cookies.set('NYT-S', open('private/NYT-S-cookie').read())

    def get_dimensions(self, response) -> tuple:
        """Get the dimensions of the crossword board.

        Parameters
        ----------
        response : requests.Response
            Response from the New York Times website.

        Returns
        -------
        tuple
            Dimensions of the crossword board.
        """
        data = response.json()
        return (data['body'][0]['dimensions']['width'],
                data['body'][0]['dimensions']['height'])

    def get_crossword_board(self, board_type, date) -> Board:
        """Get the crossword board from the New York Times website.

        Parameters
        ----------
        board_type : str
            Type of crossword board to get. Options are 'mini' and
            'crossword'.

        date : datetime.date
            Date of the crossword board to get.

        Returns
        -------
        CrosswordBoard
            Crossword board from the New York Times website.
        """
        if board_type not in self.__board_info_endpoint:
            raise ValueError(f'Invalid board type: {board_type}')
        if not isinstance(date, date):
            raise TypeError(f'Invalid date type: {type(date)}')
        if date > date.today():
            raise ValueError(f'Invalid date: {date}')

        endpoint = self.__board_info_endpoint[board_type]
        response = self._session.get(endpoint.format(date))
        response.raise_for_status()

        return self.construct_board(response)

    def construct_board(self, response) -> Board:
        """Get the crossword board from the New York Times website.

        Returns
        -------
        CrosswordBoard
            Crossword board from the New York Times website.
        """
        board = Board()

        data = response.json()
        board.set_dimensions(self.get_dimensions(response))
        for cell_no, cell in enumerate(data['body'][0]['cells']):
            answer = cell['answer'] if 'answer' in cell else ''
            board.set_cell(cell_no, answer)

        for clue in data['body'][0]['clues']:
            clue_cells = clue['cells']
            clue_direction = clue['direction'].lower()
            clue_number = int(clue['label'])
            clue_text = clue['text'][0]['plain']
            board.add_clue_position(clue_cells, clue_number, clue_direction)
            board.add_clue(clue_number, clue_direction, clue_text)

            # This isn't great design.
            answer = board.get_answer_from_cells(clue_cells)
            board.add_answer(clue_number, clue_direction, answer)

        return board


if __name__ == '__main__':
    scraper = NYTimesScraper()
    yesterday = date.today().replace(day=date.today().day - 1)
    board = scraper.get_crossword_board('mini', yesterday)
    print(board)
