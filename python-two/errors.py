try:
    f = open("./simple.txt", "r")
    f.write("Test simple")
except:
    print("ERROR: Could not find file")
finally:
    print("SUCCESS")
    f.close()

print("Hello")
