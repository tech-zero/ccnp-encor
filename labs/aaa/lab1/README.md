### AAA Lab

![AAA topology](https://github.com/tech-zero/assets/blob/main/images/aaa.png)

#### Lab Tasks:
- Enable AAA globally
- Create local user with name test, password cisco
- Configure both TACACS+ server instances, named TACACS1 and TACACS2
- Secret key set to security for both servers
- Create TACACS+ server group named T-GROUP and add both servers
- Configure AAA authentication using default method list
  - TACACS+ server group should be primary method, followed by local login, and enable password
- Enable authorization requirement for EXEC shell
  - TACACS+ server group should be primary method, followed by local login
  - Test by logging out/in to the console

[Lab Exam Items](../)
