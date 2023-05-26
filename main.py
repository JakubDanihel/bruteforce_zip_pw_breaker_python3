#importovanie kniznice na citanie zip suborov
import zipfile


#funkcia pre extraktovanie subora
def extractFile(zFile, password):
    #skusi na zaciatku extrahovat subor s pouzitim hesla v zozname
    try:
        zFile.extractall(pwd=bytes(password, 'utf-8'))
        return password
    #ak to nie je uspesne pojde o zaznam dalej
    except:
        print("skuska")
        return

#tvorba hlavnej funkcie pre extrahovanie dat zo suboru
def main():
    zfile = zipfile.ZipFile('tajne.zip')
    passFile = open('hesla.txt')
    #print(passFile)

    #loop pre prechadzanie jednotlivych hesiel v subore vzdy si zoberie jedno slovo v zozname co je oddelene enterom a ulozi si ho do premennej
    for line in passFile.readlines():
        password = line.strip('\n')
        print(password)
        #skusi pouzit heslo vo funkcii extractFile kde skusa extrahovat subor s pouzitim hesla
        guess = extractFile(zfile, password)

        #ak je heslo spravne vypise heslo a ukonci skript
        if guess:
            print('heslo je: ' + password)
            break


if __name__ == '__main__':
    main()

