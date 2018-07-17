import csv
import sqlite3
from datetime import datetime as dt

conn = sqlite3.connect('db-2.sqlite3')
c = conn.cursor()

def cargarInsuranceCompany():
    with open("insurance_companies_list.tsv", encoding="utf8") as archivo:
        for line in csv.reader(archivo, delimiter="\n"):
            d = line[0].split("\t")
            id = int(d[1])
            name = d[0]
            name = name.replace("'", "''")
            date_created = dt.now().strftime("%Y-%M-%d")
            print('INSERT INTO core_insurance_company (id, name, date_created) VALUES (',id,',',('"'+name+'"'),',','now()',');')
            c.execute('INSERT INTO core_insurance_company (id, name, date_created) VALUES (?, ?, ?)', (id, name, date_created))
            conn.commit()

def cargarCity():
    with open("city.tsv", encoding="utf8") as archivo:
        for line in csv.reader(archivo, delimiter="\n"):
            d = line[0].split("\t")
            id = int(d[1])
            name = d[0]
            date_created = dt.now().strftime("%Y-%M-%d")
            print('INSERT INTO core_city (id, name, date_created) VALUES (',id,',',('"'+name+'"'),',','now()',');')
            c.execute('INSERT INTO core_city (id, name, date_created) VALUES (?, ?, ?)', (id, name, date_created))
            conn.commit()

def cargarTitles():
    with open("titles.tsv", encoding="utf8") as archivo:
        for line in csv.reader(archivo, delimiter="\n"):
            d = line[0].split("\t")
            id = int(d[1])
            name = d[0]
            date_created = dt.now().strftime("%Y-%M-%d")
            print('INSERT INTO core_title (id, name, date_created) VALUES (',id,',',('\''+name+'\''),',','now()',');')
            c.execute('INSERT INTO core_title (id, name, date_created) VALUES (?, ?, ?)', (id, name, date_created))
            conn.commit()


def cargarLocations():
    with open("locations.tsv", encoding="utf8") as archivo:
        for line in csv.reader(archivo, delimiter="\n"):
            d = line[0].split("\t")
            id = int(d[1])
            name = d[0]
            date_created = dt.now().strftime("%Y-%M-%d")
            print('INSERT INTO core_location (id, name, date_created) VALUES (', id, ',', ('"'+name+'"'), ',', 'now()', ');')
            c.execute('INSERT INTO core_location (id, name, date_created) VALUES (?, ?, ?)', (id, name, date_created))
            conn.commit()


def cargarNeighborhoods():
    with open("neighborhoods.tsv", encoding="utf8") as archivo:
        for line in csv.reader(archivo, delimiter="\n"):
            d = line[0].split("\t")
            id = int(d[1])
            name = d[0]
            # location = int(d[2])
            date_created = dt.now().strftime("%Y-%M-%d")
            print('INSERT INTO core_neighborhood (id, name, date_created) VALUES (', id, ',', ('\''+name+'\''), ',', 'now()', ');')
            c.execute('INSERT INTO core_neighborhood (id, name, date_created) VALUES (?, ?, ?)', (id, name, date_created))
            conn.commit()
            # try:
            #     print('INSERT INTO core_location_neighborhoods (location_id, neighborhood_id) VALUES (', location, ',', id,');')
            #     #c.execute('INSERT INTO core_location_neighborhoods (id, location_id, neighborhood_id) VALUES (?, ?, ?)', (None, location, id))
            #     #conn.commit()
            #     pass
            # except:
            #     #print('no se pudo asociar un location neigh')
            #     pass


def cargarMedical():
    with open("medical.tsv", encoding="utf8") as archivo:
        for line in csv.reader(archivo, delimiter="\n"):
            d = line[0].split("\t")
            id = int(d[1])
            name = d[0]
            name = name.replace("'", "''")
            date_created = dt.now().strftime("%Y-%M-%d")
            print('INSERT INTO core_medical_school (id, name, date_created) VALUES (', id, ',', ('\''+name+'\''), ',', 'now()', ');')
            c.execute('INSERT INTO core_medical_school (id, name, date_created) VALUES (?, ?, ?)', (id, name, date_created))
            conn.commit()


def cargarUndergraduate():
    with open("undergraduate.tsv", encoding="utf8") as archivo:
        for line in csv.reader(archivo, delimiter="\n"):
            d = line[0].split("\t")
            id = int(d[1])
            name = d[0]
            date_created = dt.now().strftime("%Y-%M-%d")
            print('INSERT INTO core_undergraduate_school (id, name, date_created) VALUES (', id, ',', ('"'+name+'"'), ',', 'now()', ');')
            c.execute('INSERT INTO core_undergraduate_school (id, name, date_created) VALUES (?, ?, ?)', (id, name, date_created))
            conn.commit()


def cargarSpecialties():
    with open("specialties.tsv", encoding="utf8") as archivo:
        for line in csv.reader(archivo, delimiter="\n"):
            d = line[0].split("\t")
            id = int(d[1])
            name = d[0]
            date_created = dt.now().strftime("%Y-%M-%d")
            print('INSERT INTO core_specialty (id, name, date_created) VALUES (', id, ',', ('"'+name+'"'), ',', 'now()', ');')
            c.execute('INSERT INTO core_specialty (id, name, date_created) VALUES (?, ?, ?)', (id, name, date_created))
            conn.commit()


def cargarPractices():
    with open(r"practice.tsv", encoding="utf8") as archivo:
        for line in csv.reader(archivo, delimiter="\n"):
            d = line[0].split("\t")
            if len(d) > 10:
                id = d[0]
                name = d[1]
                name = name.replace("'", "''")
                if d[3] == 'Yes':
                    information_complete = 1
                else:
                    information_complete = 0
                if d[4] == 'Verified':
                    information_verified = 1
                else:
                    information_verified = 0
                if len(d[5])>3:
                    last_verified_date = d[5]
                else:
                    last_verified_date = "Null"

                website = d[6]
                website = website.replace("'", "''")
                neighborhood = d[9]
                location = d[11]
                city = d[13]
                address = d[14]
                address = address.replace("'", "''")
                yelp_link = d[15]
                phone = d[16]
                if len(d[16])>4:
                    phone = d[16]
                    phone = phone.replace("'", "''")
                    phhone = phone.replace("\"", "\'")
                else:
                    phone = "Null"

                single_practitioner_location = d[17]
                if d[17] == '"Yes"':
                    single_practitioner_location = 1
                else:
                    single_practitioner_location = 0
                if len(d[18])>4:
                    email = d[18]
                    email = email.replace("'", "''")
                    email = email.replace("\"", "\'")
                else:
                    email = "Null"
                if len(d[19])>4:
                    services = d[19]
                else:
                    services = "Null"
                services = services.replace("'", "''")
                date_created = dt.now().strftime("%Y-%M-%d")

                print('INSERT INTO core_practice (id, name, information_complete, information_verified, last_verified_date, website, address, yelp_link, phone, email,date_created) '
                      'VALUES (', id, ',',('\''+(name.replace("\"", "\'"))+'\''),',',information_complete ,',',information_verified ,',',last_verified_date ,',',('\''+(website.replace("\"", "\'"))+'\''), ',', ('\''+address+'\''), ',', ('\''+yelp_link+'\''), ',',('\''+phone+'\''), ',', ('\''+email+'\''),',', date_created, ');')
                # c.execute('INSERT INTO core_practice (id, name, information_complete, information_verified, website, address, yelp_link, phone, email, date_created) '
                #           'VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (id, name, information_complete, information_verified, website, address, yelp_link, phone, email, date_created))
                # conn.commit()
                # try:
                print('INSERT INTO core_practice_neighborhoods (practice_id, neighborhood_id) VALUES (',id, ',',neighborhood, ');')
                #     c.execute('INSERT INTO core_practice_neighborhoods VALUES (?, ?, ?)', (None, id, neighborhood))
                #     conn.commit()
                #     pass
                # except Exception as e:
                #     print("fallo al insertar practice", str(e))
                #     pass


def eliminarNoyelp():
    #c.execute("delete from core_practice where yelp_link not like '%yelp%'")
    #conn.commit()
    pass


def cargarPractitioners():
    with open("practitioner_only.tsv", encoding="utf8") as archivo:
        for line in csv.reader(archivo, delimiter="\n"):
            d = line[0].split("\t")
            if d.__len__() > 34:
                id = int(d[3])
                first_name = d[0]
                if first_name[first_name.__len__()-1] == ' ': first_name = first_name[:-1]
                last_name = d[1]
                information_verified = d[4]
                information_completed = d[5]
                gender = d[7]
                link_to_bio = d[8]
                short_bio = d[9]
                all_specialties = d[16]
                first_visit_price = d[22]
                follow_up_visit_price = d[23]
                prices_reflect_community_acupuncture = d[24]
                accepts_insurance = d[25]
                email = d[29]
                personal_yelp_link = d[30]
                try:
                    license_date = (dt.strptime(d[30], '%B %d, %Y')).strftime("%Y-%m-%d")
                except:
                    license_date = ''
                awards = d[35]
                group_affiliations = d[36]
                date_created = "CURRENT_TIMESTAMP"
                photo_saved = first_name + "_" + last_name.replace(" ","-") + ".jpg"
                photo_saved = photo_saved.strip().replace(" ","_")
                ids = [10,20,23,24,25,26,70,72,79,80,81]
                try:
                    print('INSERT INTO core_practitioner (id, first_name, last_name, gender, link_to_bio, '
                            'short_bio, first_visit_price, follow_up_visit_price, '
                            'prices_reflect_community_acupuncture, accepts_insurance, email, personal_yelp_link, '
                            'license_date, awards, group_affiliations, date_created, all_specialties, photo_saved, information_verified, information_complete) '
                            'VALUES (',id,',',('"'+first_name+'"'),',',('"'+last_name+'"'),',',('"'+gender+'"'),',',('"'+link_to_bio+'"'),',',('"'+short_bio+'"'),',',
                            ('"' + first_visit_price + '"'),',',('"'+follow_up_visit_price+'"'),',',('"'+prices_reflect_community_acupuncture+'"'),',',
                            ('"' + accepts_insurance + '"'),',',('"'+email+'"'),',',('"'+personal_yelp_link+'"'),',',('"'+license_date+'"'),',',('"'+awards+'"'),',',
                            ('"' + group_affiliations + '"'), ',', date_created , ',', ('"'+all_specialties+'"'), ',', ('"'+photo_saved+'"'), ',', ('"'+information_verified+'"'), ',', ('"'+information_completed+'"'),');')

                    # c.execute('INSERT INTO core_practitioner (id, first_name, last_name, gender, link_to_bio, '
                    #       'short_bio, first_visit_price, follow_up_visit_price, '
                    #       'prices_reflect_community_acupuncture, accepts_insurance, email, personal_yelp_link, '
                    #           'license_date, awards, group_affiliations, date_created, all_specialties, photo_saved, information_verified, information_complete) VALUES (?,?,?,?,?,?,?,'
                    #       '?,?,?,?,?,?,?,?,?,?,?)', (id, first_name, last_name, gender, link_to_bio, short_bio,
                    #                              first_visit_price, follow_up_visit_price,
                    #                              prices_reflect_community_acupuncture,accepts_insurance,
                    #                              email, personal_yelp_link, license_date, awards,
                    #                                  group_affiliations, date_created, all_specialties, photo_saved, information_verified, information_completed))
                    # conn.commit()
                except Exception as e:
                    #print("error al insertar practitioner", str(e))
                    pass
                # try:
                #     # if d[28] != '' and d[28] is not None:
                #     print(
                #         'INSERT INTO core_medical_school_practitioners (medical_school_id, practitioner_id) VALUES (',
                #         d[32], ',', id, ');')
                #     c.execute('INSERT INTO core_medical_school_practitioners (id, medical_school_id, practitioner_id) VALUES (?, ?, ?)',
                #                 (None, int(d[32]), id))
                #     conn.commit()
                #     pass
                # except Exception as e:
                #     #print(str(e))
                #     pass
                # try:
                #     if d[30] != '' and d[30] is not None:
                #         print('INSERT INTO core_undergraduate_school_practitioners (undergraduate_school_id, practitioner_id) VALUES (', int(d[30]), ',',id, ');')
                #         # c.execute('INSERT INTO core_undergraduate_school_practitioners (id, undergraduate_school_id, practitioner_id) VALUES (?, ?, ?)',
                #         #          (None, int(d[30]), id))
                #         # conn.commit()
                #         pass
                # except Exception as e:
                #     #print(str(e))
                #     pass

                titles = d[6].split(",")
                for i in titles:
                    try:
                        if i.strip() == 'BCSORM':
                            i = 1
                        elif i.strip() == 'C.H.':
                            i = 2
                        elif i.strip() == 'C.M.D. (China)':
                            i = 3
                        elif i.strip() == 'C.M.T.':
                            i = 4
                        elif i.strip() == 'DACM':
                            i = 5
                        elif i.strip() == 'DAOM':
                            i = 6
                        elif i.strip() == 'DC':
                            i = 7
                        elif i.strip() == 'DIPL':
                            i = 8
                        elif i.strip() == 'Dipl.Ac.':
                            i = 9
                        elif i.strip() == 'Dipl.O.M.':
                            i = 10
                        elif i.strip() == 'FABORM':
                            i = 11

                        elif i.strip() == 'L.Ac.':
                            i = 12
                        elif i.strip() == 'LMP':
                            i = 13
                        elif i.strip() == 'LMT/CMT':
                            i = 14
                        elif i.strip() == 'M.C.S.T.M.':
                            i = 15
                        elif i.strip() == 'M.S.':
                            i= 16
                        elif i.strip() == 'MD':
                            i = 17
                        elif i.strip() == 'MSOM':
                            i = 18
                        elif i.strip() == 'MSTCM':
                            i = 19
                        elif i.strip() == 'MTCM':
                            i = 20
                        elif i.strip() == 'MTOM':
                            i = 21
                        elif i.strip() == 'NC':
                            i = 22
                        elif i.strip() == 'ND':
                            i = 23
                        elif i.strip() == 'O.M.D.':
                            i = 24
                        elif i.strip() == 'PH.D.':
                            i = 25
                        elif i.strip() == 'QME':
                            i = 26
                        elif i.strip() == 'R.N.':
                            i = 27
                        elif i.strip() == 'TCM':
                            i = 28
                        else:
                            i = None
                        if i != '' and i is not None:
                            # print(
                            #     'INSERT INTO core_title_practitioners (practitioner_id, title_id) VALUES (',
                            #     id, ',', i, ');')
                            # print(
                            #     'INSERT INTO core_practitioner_titles (practitioner_id, title_id) VALUES (',
                            #     id, ',', i, ');')

                            # c.execute(
                            #     'INSERT INTO core_title_practitioners (practitioner_id, title_id) VALUES ( ?, ?)',
                            #     (id, i))
                            # conn.commit()
                            # c.execute(
                            #     'INSERT INTO core_practitioner_titles (practitioner_id, title_id) VALUES ( ?, ?)',
                            #     (id, i))
                            # conn.commit()
                            pass
                    except Exception as e:
                        #print(str(e))
                        pass
                # try:
                #     d[11] = int(d[11])
                #     print(
                #         'INSERT INTO core_specialty_practitioners (practitioner_id, specialty_id) VALUES (',
                #         id, ',', int(d[11]), ');')
                #     print(
                #         'INSERT INTO core_practitioner_specialties (practitioner_id, specialty_id) VALUES (',
                #         id, ',', int(d[11]), ');')
                #     c.execute('INSERT INTO core_specialty_practitioners (id, practitioner_id, specialty_id) VALUES (?, ?, ?)',
                #             (None, id, int(d[11])))
                #     conn.commit()
                #     c.execute(
                #     'INSERT INTO core_practitioner_specialties (id, practitioner_id, specialty_id) VALUES (?, ?, ?)',
                #     (None, id, int(d[11])))
                #     conn.commit()
                #     pass
                # except Exception as e:
                #     #print("error al bindear con specialty ",id," ", str(d[8]))
                #     if 'invalid' not in str(e):
                #         #print(str(id) + " " + str(d[8]))
                #         pass
                # try:
                #     d[13] = int(d[13])
                #     print(
                #         'INSERT INTO core_specialty_practitioners (practitioner_id, specialty_id) VALUES (',
                #         id, ',', int(d[13]), ');')
                #     print(
                #         'INSERT INTO core_practitioner_specialties (practitioner_id, specialty_id) VALUES (',
                #         id, ',', int(d[13]), ');')
                #     c.execute(
                #         'INSERT INTO core_specialty_practitioners (id, practitioner_id, specialty_id) VALUES (?, ?, ?)',
                #         (None, id, d[13]))
                #     conn.commit()
                #     c.execute(
                #         'INSERT INTO core_practitioner_specialties (id, practitioner_id, specialty_id) VALUES (?, ?, ?)',
                #         (None, id, d[13]))
                #     conn.commit()
                # except Exception as e:
                #     #print("error al bindear con specialty ", id, " ", str(d[10]))
                #     if 'invalid' not in str(e):
                #         #print(str(id) + " " + str(d[10]))
                #         pass
                # try:
                #     d[15] = int(d[15])
                #     print(
                #         'INSERT INTO core_specialty_practitioners (practitioner_id, specialty_id) VALUES (',
                #         id, ',', int(d[15]), ');')
                #     print(
                #         'INSERT INTO core_practitioner_specialties (practitioner_id, specialty_id) VALUES (',
                #         id, ',', int(d[15]), ');')
                #     c.execute(
                #         'INSERT INTO core_specialty_practitioners (id, practitioner_id, specialty_id) VALUES (?, ?, ?)',
                #         (None, id, d[15]))
                #     conn.commit()
                #     c.execute(
                #         'INSERT INTO core_practitioner_specialties (id, practitioner_id, specialty_id) VALUES (?, ?, ?)',
                #         (None, id, d[15]))
                #     conn.commit()
                # except Exception as e:
                #     #print("error al bindear con specialty ", id, " ", str(d[12]))
                #     if 'invalid' not in str(e):
                #         #print(str(id) + " " + str(d[12]))
                #         pass


def cargarPracticePractitioner():
    with open("practice_practitioner.tsv", encoding="utf8") as archivo:
        for line in csv.reader(archivo, delimiter="\n"):
            d = line[0].split("\t")
            if d.__len__() > 2:
                try:
                    practitioner_id = d[17]
                    practice_id = d[18]
                    print(
                        'INSERT INTO core_practice_practitioners (practice_id, practitioner_id) VALUES (',
                        practice_id, ',', practitioner_id, ');')
                    c.execute('INSERT INTO core_practice_practitioners (practice_id, practitioner_id) VALUES ( ?, ?)',
                             (practice_id, practitioner_id))
                    conn.commit()
                except Exception as e:
                    #print("fallo al asociar practice practitioner", str(e))
                    pass


def eliminarHuerfanos():
    #c.execute('delete from core_practitioner where id in (select id from core_practitioner where id not in (select practitioner_id from core_practice_practitioners))')
    #conn.commit()
    pass


def arreglarFotos():
    practitioners = c.execute('SELECT * FROM core_practitioner').fetchall()
    for p in practitioners:
        elpracti = str(p[1]) + " " + str(p[2])
        id = int(p[0])
        encontrado = False
        extencorrecta = ""
        nombre = str(p[17]).split(".")[0]
        try:
            archi = open(nombre + ".jpg")
            encontrado = True
            extencorrecta = ".jpg"
        except:
            pass
        try:
            archi = open(nombre + ".jpeg")
            encontrado = True
            extencorrecta = ".jpeg"
        except:
            pass
        try:
            archi = open(nombre + ".png")
            encontrado = True
            extencorrecta = ".png"
        except:
            pass
        try:
            archi = open(nombre + ".gif")
            encontrado = True
            extencorrecta = ".gif"
        except:
            pass
        try:
            archi = open(nombre + ".webp")
            encontrado = True
            extencorrecta = ".webp"
        except:
            pass
        if encontrado:
            print('UPDATE core_practitioner SET photo_saved = ',('"'+nombre+extencorrecta+'"'),' WHERE id = ',id,';')
            #c.execute('UPDATE core_practitioner SET photo_saved = ? WHERE id = ?', ((nombre+extencorrecta), id))
            #conn.commit()
        else:
            print('UPDATE core_practitioner SET photo_saved = "null.jpg" WHERE id = ', id, ';')
            #c.execute('UPDATE core_practitioner SET photo_saved = ? WHERE id = ?', ("null.jpg", id))
            #conn.commit()
            print("No pudimos encontrar la foto de: ", elpracti)


def cargarPractitionersError():
    with open("partitioner_only_error_2.tsv", encoding="utf8") as archivo:
        for line in csv.reader(archivo, delimiter="\n"):
            d = line[0].split("\t")
            if d:
                id = d[2]
                first_name = d[0]
                if first_name[first_name.__len__()-1] == ' ': first_name = first_name[:-1]
                last_name = d[1]
                information_verified = d[8]
                information_completed = d[9]
                gender = d[3]

                first_visit_price = d[4]
                follow_up_visit_price = d[5]

                accepts_insurance = d[6]


                date_created = "CURRENT_TIMESTAMP"
                photo_saved = first_name + "_" + last_name.replace(" ","-") + ".jpg"
                photo_saved = photo_saved.strip().replace(" ","_")

                print('INSERT INTO core_practitioner (id, first_name, last_name, gender,first_visit_price, follow_up_visit_price, accepts_insurance,date_created, photo_saved, information_verified, information_complete) '
                            'VALUES (',id,',',('"'+first_name+'"'),',',('"'+last_name+'"'),',',('"'+gender+'"'),
                      ',',('"' + first_visit_price + '"'),',',('"'+follow_up_visit_price+'"'),',',
                            ('"' + accepts_insurance + '"'), ',', date_created , ',', ('"'+photo_saved+'"'), ',', ('"'+information_verified+'"'), ',', ('"'+information_completed+'"'),');')


if __name__ == '__main__':

    # cargarTitles()
    # cargarLocations()
    # cargarNeighborhoods()
    # cargarCity()
    # cargarMedical()
    # cargarInsuranceCompany()
    # cargarSpecialties()
    # cargarPractices()
    # cargarPractitioners()
    # cargarPractitionersError()
    # cargarUndergraduate()



    #eliminarNoyelp()
    
    # cargarPracticePractitioner()
    #eliminarHuerfanos()
    # arreglarFotos()
