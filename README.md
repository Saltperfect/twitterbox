This readme section is yet to be framed. The api.py and db_c.py are the two main project handlers. Config.ini is to be set by the 
user.
api.py will run the project
The project is in development phase but all the basic requirements are met.
The basic funtionalities implemented are

1. search for text queries
2. get trending topics
3. save search results to db
4. save to csv
5. access database, get data (get next data, get next n data)
6. search for small strings in o/p dataset 
7. sort the db access query result by name
8. save results to csv
9. search by date

other not important add ons added later were
- added retweet, like counts
- added filters of retweet and like count(=,>,<=) and also for date range and user name
- added functions to configure and (re)initialise database (config.ini file)
- added functions to configure and (re)initialise twitter authentication  (config.ini file)
- added export to csv function for search result also
- database information needs to be kept in config.ini, it is set using a function in api.py
- twitter authentication information can either be kept in config.ini or can be passed when the API object is created
