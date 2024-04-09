def make_album(singer_name,album_name):
    album_info={'singer_name':singer_name,'album_name':album_name,}
    return album_info

i=1
while i<=3:
    print(make_album(input(),input()))
    i=i+1