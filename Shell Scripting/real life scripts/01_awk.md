## AWK
```
🔹 What is awk?

awk is a powerful text-processing tool in Linux/Unix.

It’s used for:

Pattern scanning

Text manipulation

Reports & data extraction

Works line by line, splits lines into fields (columns), and allows conditional processing.

🔹 Basic Syntax
awk 'pattern { action }' filename


pattern → Optional; specifies which lines to process.

action → What to do on matching lines (like print, calculate, etc.).

filename → The file to read.

🔹 Common Features

Field-based processing

$1, $2, … → first, second, … field of a line (fields separated by whitespace by default)

awk '{ print $1 }' file.txt


Prints the first column of every line.

Pattern matching

awk '/error/ { print $0 }' logfile.txt


Prints all lines containing error.

Field separator

awk -F, '{ print $2 }' file.csv


-F, tells awk that fields are comma-separated, useful for CSV files.

Built-in variables

NR → current line number

NF → number of fields in current line

awk '{ print NR, NF, $0 }' file.txt


Prints line number, number of fields, and the whole line.

Arithmetic & string operations

awk '{ sum += $3 } END { print sum }' file.txt


Sums the 3rd column across all lines.

Example

Suppose data.txt contains:

Alice 100
Bob 200
Charlie 150

```
awk '{ print $1 " scored " $2 }' data.txt
