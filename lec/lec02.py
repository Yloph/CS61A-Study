## Assignment is a simple means of abstraction: binds names to values
## Function definition is a powerful means of abstraction: binds names to expressions

## Execution procedure for def statement:
# 1. Set the body of that function with signature
# 2. Set the body of that function to be everything indented after the first line
# 3. Bind name to the function in the current frame

## Procedure for calling user-defined function:
# 1. Add a local frame, forming a new environment
# 2. Bind the functions formal parameters to its arguments in that frame
# 3. Execute the body of the function in that new environment

## Every expression is evaluated in the context of an environment
# Environment is the memory that keeps the track of the correspondence between names and values
# 1. An environment is a sequence of frames
# 2. A name evaluates to the value bound to that name in the earliest frame of the current environment where that name is found


## Execution rule for assignment statements:
# 1. Evaluate all expressions to the right of = from left to right
# 2. Bind all names to the left of = to the resulting values in the current frame

## print and None
# None indicates that nothing has been returned some function
# None is not displayed by the interpreter as the value of an expression

## Pure Function: just return values
## Non-pure Function: have side effects