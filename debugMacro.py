from sokoban import Warehouse
from solveSokoban import solve_sokoban_macro

def test_solve_sokoban_macro():
    puzzle_t2 ='#######\n#@ $ .#\n#######'
    wh = Warehouse()    
    wh.extract_locations(puzzle_t2.split(sep='\n'))
    # first test
    answer=solve_sokoban_macro(wh)
    expected_answer = [((1, 3), 'Right'), ((1, 4), 'Right')]
    fcn = test_solve_sokoban_macro
    print('<<  First test of {} >>'.format(fcn.__name__))
    if answer==expected_answer:
        print(fcn.__name__, ' passed!  :-)\n')
    else:
        print(fcn.__name__, ' failed!  :-(\n')
        print('Expected ');print(expected_answer)
        print('But, received ');print(answer)

test_solve_sokoban_macro()