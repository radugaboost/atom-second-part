def creating_tables(cur):
    cur.execute("create table mission\
                (id text primary key not null,\
                name text not null);")

    cur.execute("create table rocket\
                (id int primary key generated always as identity,\
                name text not null,\
                type text not null)")

    cur.execute("create table launch\
                (id int primary key generated always as identity,\
                mission_id text references mission not null,\
                rocket_id int references rocket not null)")
    return "All tables are created"

def filling_db(data: dict, cur):
    for item in data["launches"]:
        cur.execute(f"insert into mission (id, name)\
                    values ('{item['mission_id'][0]}', '{item['mission_name']}');")
        cur.execute(f"select id from rocket where\
            name='{item['rocket']['rocket_name']}' and type='{item['rocket']['rocket_type']}'")
        if not cur.fetchone():
            cur.execute(f"insert into rocket (name, type)\
                values ('{item['rocket']['rocket_name']}', '{item['rocket']['rocket_type']}')")

    for item in data["launches"]:
        cur.execute(f"select id from rocket where\
        name='{item['rocket']['rocket_name']}' and type='{item['rocket']['rocket_type']}'")
        cur.execute(f"insert into launch (rocket_id, mission_id)\
            values('{cur.fetchone()[0]}', '{item['mission_id'][0]}')")
    
    return "All data got into the database"
