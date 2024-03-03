
<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h3 align="center">Sample python server and client project</h3>

  <p align="center">
    A sample project
    <br />
    <a href="https://github.com/mahyarkarimi/simple-python-server-client"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/mahyarkarimi/simple-python-server-client/issues">Report Bug</a>
    ·
    <a href="https://github.com/mahyarkarimi/simple-python-server-client/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

It is a python server and client application that its intended to achieve the common goal to downloads a certain set of resources, merges them with CSV-transmitted resources, and converts them to a formatted excel file.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python][Python]][Python-url]
* [![FastAPI][FastAPI]][FastAPI-url]
* [![Pandas][Pandas]][Pandas-url]
* [![Docker][Docker]][Docker-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

You need to install `python3.10` or higher in order to run the server and client locally.
To start server as a docker container you must install `docker` and `docker compose`.


### Installation

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

1. Clone the repo
   ```sh
   git clone https://github.com/mahyarkarimi/simple-python-server-client.git
   ```
2. Create a virtual environment and activate it
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install Pip packages
   ```sh
   pip install -r requirements.txt
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->
## Usage

To use the client CLI tool you must first start the server. To start te server you must either serve it with `uvicorn` or start the `docker compose service`. Open a terminal in your system and enter the following to start a server locally with uvicorn:

  ```sh
  uvicorn server:main --port 5000
  ```

Or enter the following to start the server container:

  ```sh
  docker compose up -d
  ```

* Make sure that port number 5000 is not used in your system, otherwise try to change it by setting the `PORT` environment variable in .env file in project root and in uvicorn command.

After successful start of server, you can use the client, e.g.

  ```sh
  python3 client.py vehicles.csv --keys gruppe,kurzname,langtext,info,lagerort -c
  ```

You can also read the help of the CLI tool by passing `-h` argument to client.py (e.g. `python3 client.py -h`)

  ```sh
  usage: vehicleTest [-h] -k KEYS -c filepath

  It is a CLI tool to connect with the merge API to retreive the information of cars

  positional arguments:
    filepath              Path to the csv file

  options:
    -h, --help            show this help message and exit
    -k KEYS, --keys KEYS  Names of the columns (if more than one column is specified it should be separated by comma e.g. --keys
                          info,lagerort,labelIds)
    -c, --colored         Set this field to colorize the texts of each row based on labelIds colorCode

  Example usage: $ python3 client.py vehicles.csv --keys info,lagerort,labelIds -c
  ```


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Your Name - mahyarkarimi@rocketmail.com

Project Link: [https://github.com/mahyarkarimi/simple-python-server-client](https://github.com/mahyarkarimi/simple-python-server-client)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

[Python]: https://img.shields.io/badge/python-000000?style=for-the-badge&logo=python
[Python-url]: https://python.org/
[FastAPI]: https://img.shields.io/badge/fastapi-20232A?style=for-the-badge&logo=fastapi&logoColor=61DAFB
[FastAPI-url]: https://fastapi.tiangolo.com/
[Pandas]: https://img.shields.io/badge/pandas-35495E?style=for-the-badge&logo=pandas&logoColor=4FC08D
[Pandas-url]: https://pandas.pydata.org/
[Docker]: https://img.shields.io/badge/docker-0000DD?style=for-the-badge&logo=docker&logoColor=white
[Docker-url]: https://docker.com/