
This is a simple dynamically typed pseudocode interpreter (PCL) written in python. It runs the code according to the specified syntax defined in this file.

It uses Flex to act as a lexer and Bison to parse the code.

If you are using or learning psuedocode you can use this language to run simple frameworks making code more acessible and making it easier to correct mistakes when learning about pseudocode by actually testing your creations.

There are little scematics as all functions are pretty fundemental and staightforward.

Automatic variable assignment:
```
DECLARE VariableName = String/Integer/Variable/Boolean
```

Input output is handled just like so:
```
INPUT VariableName #If the variable is not defined it will create it
OUTPUT foo
```

Loops are done like so: (IB standard)
```
loop WHILE #While loop

loop I from X to Y #For loop

END loop
```

If statements look like loops:
```
IF foo THEN

bar

ELSE {IF THEN} 

bar

END IF
```

Arrays are straightforward:
```
DECLARE ArrayName: ARRAY[Length, Rows (default:0)] OF DataType
ArrayName[Index]
```

Boolean operators and operations:
```
+-
*/
%//
==/=/!=
></=><=

AND OR NOT
```

Subroutines are:
```
METHOD MathodName(ARGUMENTS)
    
    RETURN String/Integer/Variable/Boolean

END METHOD
```

Len Functions
```
#Length is always calculated and stored in the metadata of a array
#To access the lenght of your array use:

ArrayName.N

#This also goes for any variables length
```


The following functionality is defined in the standard library of PCL:


Collections
```
DECLARE CollectionName = []

#Collection functions (CollectionName.function()):

.getNext()
.hasNext()
.resetNext()
.addItem(Item)
.isEmpty()
```

File handling (as described by the A level)
```

OPENFILE "FileName" FOR READ/WRITE
CLOSEFILE "FileName"

READFILE "FileName", LineOfText #Keeps a pointer to current line, increases by one each time function is called.
WRITEFILE "FileName", String #Overwrites the line that the pointer is currently at and increases pointer by one.

FILE.resetNext() #Resets the pointer

```







