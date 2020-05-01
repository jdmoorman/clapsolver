import numpy as np
import pytest

from clapsolver import clap

# fmt: off
cost_matrix_1 = [[4, 1, 3],
                 [2, 0, 5],
                 [3, 2, 2]]

cost_matrix_2 = [[4, 1, 3, 6],
                 [2, 0, 5, 7],
                 [3, 2, 2, 8]]

cost_matrix_3 = [[4, 1, 3],
                 [2, 0, 5],
                 [3, 2, 2],
                 [6, 7, 8]]

cost_matrix_4 = [[np.inf, np.inf, np.inf, np.inf,      3],
                 [     7, np.inf,     23, np.inf, np.inf],
                 [    17,     24, np.inf, np.inf, np.inf],
                 [np.inf,      6,     13,     20, np.inf]]

cost_matrix_5 = [[4, 1, 3, np.inf],
                 [2, 0, 5, np.inf],
                 [3, 2, 2, np.inf]]

cost_matrix_6 = [[4, 1, 3],
                 [2, 0, 5],
                 [np.inf, np.inf, np.inf],
                 [3, 2, 2],
                 [6, 7, 8]]

global_cost_1 = np.array([[6, 5, 6],
                          [5, 6, 9],
                          [6, 7, 5]])

global_cost_2 = np.array([[6, 5, 6, 8],
                          [5, 6, 9, 10],
                          [6, 7, 5, 11]])

global_cost_3 = np.array([[6, 5, 6],
                          [5, 6, 9],
                          [6, 7, 5],
                          [8, 11, 11]])

global_cost_4 = np.array([[np.inf, np.inf, np.inf, np.inf,     47],
                          [    47, np.inf,     49, np.inf, np.inf],
                          [    49,     47, np.inf, np.inf, np.inf],
                          [np.inf,     49,     47,     54, np.inf]])

global_cost_5 = np.array([[6, 5, 6, np.inf],
                          [5, 6, 9, np.inf],
                          [6, 7, 5, np.inf]])

global_cost_6 = np.array([[6, 5, 6],
                          [5, 6, 9],
                          [np.inf, np.inf, np.inf],
                          [6, 7, 5],
                          [8, 11, 11]])
# fmt: on


class TestClap:
    @pytest.mark.parametrize(
        "i, j, cost_matrix, expected",
        [
            (0, 0, cost_matrix_1, 6),
            (0, 1, cost_matrix_1, 5),
            (0, 2, cost_matrix_1, 6),
            (1, 0, cost_matrix_1, 5),
            (1, 1, cost_matrix_1, 6),
            (1, 2, cost_matrix_1, 9),
            (2, 0, cost_matrix_1, 6),
            (2, 1, cost_matrix_1, 7),
            (2, 2, cost_matrix_1, 5),
            (0, 3, cost_matrix_2, 8),
            (1, 3, cost_matrix_2, 10),
            (2, 3, cost_matrix_2, 11),
            (3, 0, cost_matrix_3, 8),
            (3, 1, cost_matrix_3, 11),
            (3, 2, cost_matrix_3, 11),
        ],
    )
    def test_clap_cost(self, i, j, cost_matrix, expected):
        """Verify clap.cost works on small examples computable by hand."""
        assert clap.cost(i, j, cost_matrix) == expected

    @pytest.mark.parametrize(
        "cost_matrix, expected_global_costs",
        [
            (cost_matrix_1, global_cost_1),
            (cost_matrix_2, global_cost_2),
            (cost_matrix_3, global_cost_3),
            (cost_matrix_4, global_cost_4),
            (cost_matrix_5, global_cost_5),
            (cost_matrix_6, global_cost_6),
        ],
    )
    def test_clap_costs(self, cost_matrix, expected_global_costs):
        """Verify clap.constrained_lsap_costs works on small examples."""
        assert clap.costs(cost_matrix).tolist() == expected_global_costs.tolist()

        num_rows, num_cols = np.array(cost_matrix).shape
        for i in range(num_rows):
            for j in range(num_cols):
                assert clap.cost(i, j, cost_matrix) == expected_global_costs[i, j]
