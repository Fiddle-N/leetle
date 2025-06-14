import functools


def solve(nums):
    @functools.cache
    def max_theft(
        position=None,
    ):
        if position is not None and position >= len(nums):
            # beyond the last house
            return 0
        # must skip next house (position + 1)
        # but while we can visit position + 2
        # position + 3 might be better
        # however, start position is a special case
        # where we don't need to skip the next house
        current_theft = 0 if position is None else nums[position]
        if position is None:
            # set position to not skip next house
            position = -2
        return (
            max(
                max_theft(
                    position=position + 2,
                ),
                max_theft(
                    position=position + 3,
                ),
            )
            + current_theft
        )

    return max_theft()
