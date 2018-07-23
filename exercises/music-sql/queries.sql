SELECT Artist.ArtistName, Song.Title --selecting which table(S) to join/compare
FROM Artist --:look at this table and then...
join Song on Artist.ArtistId = song.ArtistId -- COMBINE the artistIds in Artist and Song Tables
where Artist.ArtistName = "Black Flag" -- only show Black Flag


-- 1. Query all of the entries in the Genre table
SELECT * FROM GENRE

-- 2. Using the INSERT statement, add one of your favorite artists to the Artist table.
INSERT INTO Artist (ArtistName, YearEstablished)
values ("Radiohead",  "1985")

-- 3. Using the INSERT statement, add one, or more, albums by your artist to the Album table.
INSERT INTO Album (Title, ReleaseDate, AlbumLength, Label, ArtistId, GenreId)
values ("The Bends", "03/13/1995", "2345", "Parlophone", 28, 2), ("OK Computer", "06/16/1997", "2345", "Parlophone", 28, 2)

-- 3a. In case you don't know the IDs and want to avoid hard coding them
INSERT INTO Album
select null, "Kid A", "10/02/2000", 666, "Parlophone", artist.artistid, genre.GenreId
FROM Artist, Genre
WHERE Artist.ArtistName = "Radiohead"
AND Genre.Label = "Rock"

-- 4. Using the INSERT statement, add some songs that are on that album to the Song table.
INSERT INTO Song (Title, SongLength, ReleaseDate, GenreId, ArtistId, AlbumId)
values ("Airbag", 284, "06/16/1997", 2, 28, 24), ("Paranoid Android", 383, "06/16/1997", 2, 28, 24), ("Subterranean Homesick Alien",  267, "06/16/1997", 2, 28, 24), ("Planet Telex", 259, "03/13/1995", 2, 28, 23), ("The Bends", 246, "03/13/1995", 2, 28, 23), ("High & Dry", 257, "03/13/1995", 2, 28, 23)

-- 4a. In case you don't know the IDs and want to avoid hard coding them
INSERT INTO Song
select null, "Fake Plastic Trees", 666, "03/13/1995", genre.genreid, artist.artistid, album.albumid
FROM Genre, Artist, Album
WHERE Genre.Label = "Rock"
AND Artist.ArtistName = "Radiohead"
AND Album.Title = "The Bends"

-- 5. Write a SELECT query that provides the song titles, album title, and artist name for all of the data you just entered in. Use the LEFT JOIN keyword sequence to connect the tables, and the WHERE keyword to filter the results to the album and artist you added.
SELECT Artist.ArtistName, ArtistSong.Title,  Album.Title
FROM SONG
LEFT JOIN Album ON Song.AlbumId = Album.AlbumId
LEFT JOIN Artist ON Album.ArtistId = Artist.ArtistId

-- SYNTAX OF LEFT JOIN
    -- SELECT column_name(s)
    -- FROM table1
    -- LEFT JOIN table2 ON table1.column_name = table2.column_name;

-- Reminder: Direction of join matters. Try the following statements and see the difference in results.

-- SELECT a.Title, s.Title FROM Album a LEFT JOIN Song s ON s.AlbumId = a.AlbumId;
-- SELECT a.Title, s.Title FROM Song s LEFT JOIN Album a ON s.AlbumId = a.AlbumId;

-- 6. Write a SELECT statement to display how many songs exist for each album. You'll need to use the COUNT() function and the GROUP BY keyword sequence.
SELECT COUNT(SongId) AS "Song Count", Album.Title AS "Album Title"
FROM Song
LEFT JOIN Album ON Song.AlbumId = Album.AlbumId --needs representation of what is COMMON between both tables
GROUP BY Album.Title -- Sorty By Album Title


-- 7. Write a SELECT statement to display how many songs exist for each artist. You'll need to use the COUNT() function and the GROUP BY keyword sequence.
SELECT COUNT(SongId) AS "Song Count", Artist.ArtistName AS "Artist"
FROM Song
LEFT JOIN Artist ON Song.ArtistId = Artist.ArtistId
GROUP BY Artist.ArtistName

-- 8. Write a SELECT statement to display how many songs exist for each genre. You'll need to use the COUNT() function and the GROUP BY keyword sequence.
SELECT COUNT(SongId) AS "Song Count", Genre.Label AS "Genre"
FROM Song
LEFT JOIN Genre ON Song.GenreId = Genre.GenreId
GROUP BY Genre.Label -- Sort by Genre

-- 9. Using MAX() function, write a select statement to find the album with the longest duration. The result should display the album title and the duration.
SELECT MAX(AlbumLength) AS "Album Length", Album.Title AS "Album Title" -- Here we are not joining tables but looking at two columns within the same table.  WHERE isn't necessary
FROM Album

-- 10. Using MAX() function, write a select statement to find the song with the longest duration. The result should display the song title and the duration.
SELECT MAX(SongLength) AS "Song Length", Song.Title AS "Song"
FROM Song -- Result is 'THUG'

-- 11. Modify the previous query to also display the title of the album.
SELECT MAX(SongLength) AS "Song Length", Song.Title AS "Song", Album.Title
FROM Song -- Result is 'THUG'
LEFT JOIN Album ON Song.AlbumId = Album.AlbumId