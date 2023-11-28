# Daily activities launcher with Python

Double-clicking daily.py file opens command prompt with options for the user:

* 0 - Start all
* 1 - Start programs
* 2 - Start websites in browser

Any other command cancels and closes the program.

## Program paths and website urls

Program looks for and reads files named program_paths.txt and website_urls.txt in current folder.

Both program paths and website urls need to be written line by line.

## Future considerations

* Add error-handling for missing files.
* Add feature for user to add paths and urls through the program.
* Save and load from using a database instead of txt files.
* Add feature for user to change saved data.
* Consider adding test cases.