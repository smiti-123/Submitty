def up(config, database, semester, course):
    database.execute("ALTER TABLE electronic_gradeable ADD COLUMN eg_vcs_host_type INTEGER DEFAULT 0")


def down(config, database, semester, course):
    database.execute("ALTER TABLE ONLY electronic_gradeable DROP COLUMN eg_vcs_host_type")