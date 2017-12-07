"""
Coder: Jacky Shew
Description: Calculates the Football Passer Rating statistic
"""

completion_per_attempt = 0.6627 #change Completions here
yards_per_attempt = 6.9219 #change Yards per Attempt here
touchdowns_per_attempt = 0.0486 #change Touchdowns per Attempt here
interceptions_per_attempt = 0.0250 #change Interceptions per Attempt here

passer_rating = ((((completion_per_attempt-0.3)*5+((yards_per_attempt-3))/4+touchdowns_per_attempt*20+2.375-(interceptions_per_attempt*25)))/6)*100

print("The passer rating is", passer_rating)