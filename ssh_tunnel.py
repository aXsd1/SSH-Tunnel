import pymysql
import sshtunnel

# SSH connection
ssh_host = 'server147.web-hosting.com'  #Host
ssh_port = 21098                        #Server Port
ssh_user = '******'                     #cPanel username
ssh_pass = '******'                     #cPanel password

# mySQL connection
mysql_host = '127.0.0.1'                
mysql_port = 3306                       #If this port is used by a different application, you can change it
mysql_user = '*******'                  #mySQL username
mysql_pass = '*******'                  #mySQL password
mysql_db = '*******'                    #Data base name

# SSH tunnel
with sshtunnel.SSHTunnelForwarder(
    (ssh_host, ssh_port),
    ssh_username=ssh_user,
    ssh_password=ssh_pass,
    remote_bind_address=(mysql_host, mysql_port)
) as tunnel:
    #SSH tunnel created
    #mySQL connection
    conn = pymysql.connect(
        host='127.0.0.1',
        port=tunnel.local_bind_port,
        user=mysql_user,
        passwd=mysql_pass,
        db=mysql_db
    )
    
    try:
        with conn.cursor() as cursor:
            sql = "SELECT * FROM user_data"
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                print(row)
    finally:
        conn.close()
