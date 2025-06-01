from enum import Enum, auto


class StockDecision(Enum):
    START = auto()
    PREV_BOUGHT = auto()
    JUST_SOLD = auto()
    PREV_SOLD = auto()


def solve(prices):
    def _solve(prev_decision, profit, prices):
        if not prices:
            return profit

        price = prices.pop(0)

        if prev_decision == StockDecision.PREV_BOUGHT:
            return max(
                # wait
                _solve(StockDecision.PREV_BOUGHT, profit, prices.copy()),
                # or sell
                _solve(StockDecision.JUST_SOLD, profit + price, prices.copy()),
            )

        if prev_decision == StockDecision.JUST_SOLD:
            # cooldown - must wait
            return _solve(StockDecision.PREV_SOLD, profit, prices.copy())

        if prev_decision in (StockDecision.START, StockDecision.PREV_SOLD):
            return max(
                # buy
                _solve(StockDecision.PREV_BOUGHT, profit - price, prices.copy()),
                # or wait
                _solve(StockDecision.PREV_SOLD, profit, prices.copy()),
            )

    return _solve(StockDecision.START, 0, prices.copy())


print(solve([1, 2, 3, 0, 2]))
