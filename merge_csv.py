import csv

with open('movies.csv') as f:
    

headers.append("poster_link")

with open("final.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)

with open("movie_links.csv") as f:
   

for movie_item in all_movies:
    poster_found = any(movie_item[8] in movie_link_items for movie_link_items in all_movie_links)
    if poster_found:
        for movie_link_item in all_movie_links:
           
