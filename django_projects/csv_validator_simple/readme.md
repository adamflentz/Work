# CSV Validator

REST Framework that validates CSV Files to an associated schema. Uses Frictionlessdata's goodtables API to validate to the schema.

## Getting Started
If all modules are installed through pip to the versions in requirements.txt, the service should run without any issues. All requests to the page should be formatted like so:
```
curl -H "Authorization: Token <your token>" -F docfile=@<your csv file> -F jsonfile=@<your json file> -F errorlimit=<True or False> -F order_fields=<True or False> localhost:8000/csvvalidate/

```
##Test Cases
* test1: Checks a valid CSV to a valid schema. Should return no errors.
* test2: Checks for a type mismatch within data.  Should return a non castable value error.
* test3: Checks for non-matching column names: Should return an error of non-matching headers.
* test4: Checks for a mismatch in column numbers: Will either return an error of a missing header or extra header depending on the schema and csv.
* test5: Checks whether or not values in a field are unique.  Should return an error that one row is duplicated.
