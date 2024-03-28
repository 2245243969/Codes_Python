def make_album(singer_name,album_name):
    album_info={'singer_name':singer_name,'album_name':album_name,}
    return album_info


while True:
    print(("\nPlease tell me the information about the album:"))
    print("(enter 'q' at any time to quit)")

    singer_name=input("The singer's name is:")
    if singer_name=='q':
        break

    album_name=input("The album's name is:")
    if album_name=='q':
        break

    print(make_album(singer_name,album_name))
    print("Do you wanna countinue to create a new album?(yes/no)")
    if input()=='no':
        break
