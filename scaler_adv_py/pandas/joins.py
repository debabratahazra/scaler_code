import numpy as np
import pandas as pd


users = pd.DataFrame({"userid": [1, 2, 3], "name": [
                     "Srinivas", "Prem", "Prashant"]})
msgs = pd.DataFrame({"userid": [1, 1, 2, 4], "msg": [
                    'hmm', "acha", "theek hai", "nice"]})

print("users\n", users)
print()
print("msgs\n", msgs)
print()

# vstack
vstack = pd.concat([users, msgs], axis=0)
print("concat vertical\n", vstack)

# vstack with proper implicit index
vstack = pd.concat([users, msgs], axis=0, ignore_index=True)
print("concat vertical with proper index\n", vstack)

# hstack
hstack = pd.concat([users, msgs], axis=1)
print("concat horizontal\n", hstack)


################################################################
# JOINS
print("Users:\n", users.head())
print("Message:\n", msgs.head())

# inner join
inner_join = users.merge(msgs, on="userid")
print("Inner join\n", inner_join.head())

# left join
left_join = users.merge(msgs, left_on="userid", right_on="userid", how="left")
print("Left join\n", left_join.head())

# right join
right_join = users.merge(msgs, left_on="userid",
                         right_on="userid", how="right")
print("Right join\n", right_join.head())

# full outer join
outer_join = users.merge(msgs, left_on="userid",
                         right_on="userid", how="outer")
print("Full Outer join\n", outer_join.head())
