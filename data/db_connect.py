import psycopg2

class dbHelper():
    def __init__(self):
        #db_url = "postgresql://postgres:[password]@db.ebujagqqgpbkvevfuqjl.supabase.co:5432/postgres"
        self.db_url="postgresql://postgres.ebujagqqgpbkvevfuqjl:[password]@aws-0-us-west-1.pooler.supabase.com:6543/postgres"

        self.conn = psycopg2.connect(self.db_url)

    def addWar(self, warData):
        with self.conn.cursor() as self.cursor:
            self.cursor.execute("""
                INSERT INTO wars (
                    result,
                    end_time,
                    team_size,
                    clan_tagid,
                    clan_name,
                    clan_level,
                    clan_attacks,
                    clan_stars,
                    clan_destructionper,
                    clan_expearned,
                    opponent_tagid,
                    opponent_name,
                    opponent_level,
                    opponent_stars,
                    opponent_destructionper
                )
                VALUES (
                    %(result)s,
                    %(endTime)s,
                    %(teamSize)s,
                    %(clanTag)s,
                    %(clanName)s,
                    %(clanLevel)s,
                    %(clanAttacks)s,
                    %(clanStars)s,
                    %(clanDestrPer)s,
                    %(clanExpEarn)s,
                    %(oppTag)s,
                    %(oppName)s,
                    %(oppLevel)s,
                    %(oppStars)s,
                    %(oppDestrPer)s
                )
                """, warData)

            self.conn.commit()