![Group.png](./Group.png)

## How do I envision it?
You, as a busy (bro/ho)grammer, want a command line utility that lets you type statements like

> I need to study Algorithms for 2 hours by today

Or

> spend time researching for OO Assignment est 4 hours tomorrow

Optionally, you can indicate priority with "might" _(low)_, "want" _(normal)_, "need" _(high)_

You can give an estimated figure on how long it will take by writing "for TIME" anywhere.

To be more specific, the grammar is:
```
S -> [ANY] [HELPER] VERB [NounPhrase] TACKON*
ANY -> Personal Pronoun
HELPER -> might | want | need
VERB -> study | do | read | blah
TACKON -> DURATION | CUTOFF | PLANNED_TIME
PLANNED_TIME -> from TIME (till | until) TIME | at TIME
DURATION -> (est | for) TIME
CUTTOFF -> by TIME
TIME -> [day/date] CLOCK_TIME
```

## Breakdown of Features, released first to last
* You can log any verb phrase (do this, do that) as a task
* You can see all upcoming tasks by typing
  > view
  
  and you can view old tasks by typing
  > history
  
  and you can view a specific day by typing
  > view DATE
  
  where DATE could be **tomorrow**, **today**, **24 June**, ie
  > view tomorrow

* You can give the task a cutoff or due by date by using **by TIME**, for example
  * do X by Wednesday night
  * do Y by tomorrow 
  * do Z by July 26
* You can give JUST a start time by writing **at TIME**, or give a start and end by writing **from TIME till TIME**.

These first features are going to be my focus, I'm going to plan out on Trello for the rest.
