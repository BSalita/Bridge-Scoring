# adapted (MIT license) from https://github.com/jfklorenz/Bridge-Scoring/blob/master/features/score.js
# ================================================================
# Scoring
def score(level, suit, double, declarer, vulnerability, result):
    assert level in range(0,7),f'ValueError: level {level} is invalid'
    assert suit in range(0,5),f'ValueError: suit {suit} is invalid'
    assert double in range(0,3),f'ValueError: double {double} is invalid'
    assert declarer in range(0,4),f'ValueError: declarer {declarer} is invalid'
    assert vulnerability in range(0,2),f'ValueError: vulnerability {vulnerability} is invalid'
    assert result in range(-13,7),f'ValueError: result {result} is invalid'

    # Contract Points
    points_contract = [
        [[20, 40, 80], [20, 40, 80]],
        [[20, 40, 80], [20, 40, 80]],
        [[30, 60, 120], [30, 60, 120]],
        [[30, 60, 120], [30, 60, 120]],
        [[40, 80, 160], [30, 60, 120]]
        ]

    # Overtrick Points
    overtrick = [
        [[20, 100, 200], [20, 200, 400]],
        [[20, 100, 200], [20, 200, 400]],
        [[30, 100, 200], [30, 200, 400]],
        [[30, 100, 200], [30, 200, 400]],
        [[30, 100, 200], [30, 200, 400]]
        ]

    # Undertrick Points
    undertricks = [
        [[50, 50, 50, 50], [100, 200, 200, 300], [200, 400, 400, 600]],
        [[100, 100, 100, 100], [200, 300, 300, 300], [400, 600, 600, 600]]
        ]

    # Bonus Points
    bonus_game = [[50, 50], [300, 500]]
    bonus_slam = [[500, 750], [1000, 1500]]
    bonus_double = [0, 50, 100]

    if result >= 0:
        points = points_contract[suit][0][double] + level * points_contract[suit][1][double]
        
        points += bonus_game[points >= 100][vulnerability]

        if level >= 5:
            points += bonus_slam[level - 5][vulnerability]

        points += bonus_double[double] + result * overtrick[suit][vulnerability][double]

    else:
        points = -sum([undertricks[vulnerability][double][min(i,3)] for i in range(0, -result)])
                         
    return points if declarer < 2 else -points # negate points if EW

# ================================================================
                         
