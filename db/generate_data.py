#!/usr/bin/env python3

from randomuser import RandomUser
import random
import time
import psycopg as pg
import uuid

from datetime import timedelta, datetime

NUM_USERS=100
NUM_FACILITIES=20
MAX_ACCESS_PER_USER=20
CONNECTION_DATA="dbname='ipm2122_db' host='localhost' port='5438' user='ipm2122_user' password='secret'" 

def random_dates(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second_1 = random.randrange(int_delta)
    random_second_2 = random_second_1 + random.randrange(60*60*8)
    return start + timedelta(seconds=random_second_1), start + timedelta(seconds=random_second_2)


if __name__ == "__main__":

    user_list = RandomUser.generate_users(NUM_USERS, {'nat': 'es'})

    conn = pg.connect(CONNECTION_DATA)
    cur = conn.cursor()
    user_ids = []

    cur.execute("DELETE FROM access_log")
    cur.execute("DELETE FROM facilities")
    cur.execute("DELETE FROM users")

    print("Inserting users...", end=' ', flush=True)
    for user in user_list:
        user_id = str(uuid.uuid4())
        user_ids.append(user_id)
        username = user.get_username()
        password = user.get_password()
        name = user.get_first_name()
        surname = user.get_last_name()
        email = user.get_email()
        is_vaccinated = bool(random.getrandbits(1))
        phone = user.get_phone()
        
        cur.execute("""
            INSERT INTO users(
                    uuid, 
                    username, 
                    password, 
                    name, 
                    surname, 
                    email, 
                    is_vaccinated, 
                    phone)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
            """, (user_id, username, password, name, surname, email, is_vaccinated, phone)
        )

    print("done")

    print("Inserting facilities...", end=' ', flush=True)
    facility_list = RandomUser.generate_users(NUM_FACILITIES, {'nat': 'es'})
    facility_types = ["Edificio", "Biblioteca", "Polideportivo", "Estadio", "Centro cultural", "Centro comercial"]
    facility_ids = []
    for facility in facility_list:
        facility_name = f"{random.choice(facility_types)} {facility.get_first_name()} {facility.get_last_name()}"
        address = facility.get_street()
        max_capacity = random.randrange(50, 300, 10)
        percentage_capacity_allowed = random.randrange(30, 100, 10)
        cur.execute(""" 
            INSERT INTO facilities(
                    name,
                    address,
                    max_capacity,
                    percentage_capacity_allowed)
                VALUES (%s,%s,%s,%s) RETURNING id
            """, (facility_name, address, max_capacity, percentage_capacity_allowed)
        )
        facility_id = cur.fetchone()[0]
        facility_ids.append(facility_id)

    print("done")

    print("Inserting access logs...")
    today = datetime.today()
    last_month = datetime.today() - timedelta(days=30)
    n = 0
    for user_id in user_ids:
        print("\t- user", n)
        n +=1
        for i in range(random.randrange(10,MAX_ACCESS_PER_USER)):
            facility_id = random.choice(facility_ids)
            date_in, date_out = random_dates(last_month, today)
            temperature = float(random.randrange(350, 375))/10
            cur.execute(""" 
                INSERT INTO access_log(
                        user_id,
                        facility_id,
                        type,
                        timestamp,
                        temperature)
                    VALUES(%s, %s, %s, %s, %s)
                """, (user_id, facility_id, "IN", str(date_in), str(temperature)) )
        
            cur.execute(""" 
                INSERT INTO access_log(
                        user_id,
                        facility_id,
                        type,
                        timestamp,
                        temperature)
                    VALUES(%s, %s, %s, %s, %s)
                """, (user_id, facility_id, "OUT", str(date_out), str(temperature)) )
    print("done")
    conn.commit()
    cur.close()
    conn.close()
