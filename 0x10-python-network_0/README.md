# 0x10-python-network_0

## General

1. What a URL is

A URL (Uniform Resource Locator) is a string of characters that provides a way to identify and locate resources on the internet. It specifies the protocol, domain, path, query parameters, and other components required to access a specific resource.

2. What HTTP is

HTTP (Hypertext Transfer Protocol) is an application-level protocol used for transmitting hypermedia documents, such as HTML files, over the internet. It defines the rules for communication between clients (such as web browsers) and servers.

3. How to read a URL

To read a URL, you can break it down into its components:

- Scheme: Specifies the protocol used, such as HTTP or HTTPS.
- Domain: Represents the network location or the web address, typically in the format "www.example.com".
- Port: (Optional) Specifies the communication endpoint on the server. Default ports are used if not explicitly stated.
- Path: Identifies the specific resource or file on the server.
- Query String: (Optional) Contains additional parameters in the form of key-value pairs, separated by ampersands (&).
- Fragment: (Optional) Points to a specific section within the document.

4. The scheme for a HTTP URL

The scheme for a HTTP URL is "http://" for non-encrypted connections or "https://" for encrypted connections (secured with SSL/TLS).

5. What a domain name is

A domain name is a human-readable label used to identify a website or a network domain. It typically consists of a string of characters separated by dots, representing a hierarchy of sub-domains and the top-level domain.

6. What a sub-domain is

A sub-domain is a subdivision of a larger domain, typically used to organize and categorize specific sections or services of a website. It appears before the main domain name and is separated by a dot. For example, "subdomain.example.com".

7. How to define a port number in a URL

A port number in a URL is defined by appending a colon (:) followed by the port number after the domain. For example, "example.com:8080" specifies the use of port 8080 for communication.

8. What a query string is

A query string is a part of a URL that contains additional parameters and their values, used to pass information to the server. It starts with a question mark (?) and consists of key-value pairs separated by ampersands (&).

9. What an HTTP request is

An HTTP request is a message sent by a client (such as a web browser) to a server, requesting a specific resource or action. It includes information such as the HTTP method (GET, POST, etc.), headers, and, in some cases, a message body.

10. What an HTTP response is

An HTTP response is the message sent by a server to a client in response to an HTTP request. It contains the requested resource or an indication of the outcome of the request. It includes a status code, headers, and, optionally, a message body.

11. What HTTP headers are

HTTP headers are additional information included in an HTTP request or response. They provide metadata about the message and can include details such as the content type, content length, caching instructions, and more.

12. What the HTTP message body is

The HTTP message body is the optional part of an HTTP request or response that contains the actual data being sent. It can include HTML content, JSON data, files, or any other type of payload.

13. What an HTTP request method is

An HTTP request method is an action or operation to be performed on a resource by an HTTP client. Common methods include GET (retrieve resource), POST (submit data), PUT (update resource), DELETE (remove resource), and more.

14. What an HTTP response status code is

An HTTP response status code is a three-digit number sent by a server to indicate the outcome of an HTTP request. Examples include 200 (OK), 404 (Not Found), 500 (Internal Server Error), and many others. Each status code carries a specific meaning.

15. What an HTTP Cookie is

An HTTP Cookie is a small piece of data stored on the client-side by a web server. Cookies are used to maintain stateful information, such as user preferences or session data, between multiple HTTP requests.

16. How to make a request with cURL

To make a request with cURL, you can use the command-line tool with various options and flags to specify the desired HTTP method, headers, data, and more.

17. What happens when you type google.com in your browser (Application level)

When you type "google.com" in your browser, at the application level, the browser initiates an HTTP GET request to the server associated with "google.com". The server processes the request, generates an HTML response containing the Google homepage, and sends it back as an HTTP response. The browser then renders and displays the HTML content, allowing you to interact with the Google search page.
