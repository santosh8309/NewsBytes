# NewsBytes
hosted_address: http://ec2-18-219-86-120.us-east-2.compute.amazonaws.com/
Usage:
1. Enter the URL for encryption
2. URL will be displayed over the page

Why SHA256:
Using SHA256 hashing algorithm
1. it is easy to compute the hash value for any given URL
2. it is infeasible to generate a URL that has a given hash
3. it is infeasible to modify a URL without changing the hash
4. it is infeasible to find two different URLs with the same hash.
Files:
->templates folder contains HTML page, 
->NB_Server is a Flask app
