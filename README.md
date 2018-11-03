# COOPER to stdout

[![Travis](https://img.shields.io/travis/hardwario/cp2stdout/master.svg)](https://travis-ci.org/hardwario/cp2stdout)
[![Release](https://img.shields.io/github/release/hardwario/cp2stdout.svg)](https://github.com/hardwario/cp2stdout/releases)
[![License](https://img.shields.io/github/license/hardwario/cp2stdout.svg)](https://github.com/hardwario/cp2stdout/blob/master/LICENSE)

## Installing

You can install **cp2stdout** directly from PyPI:

```sh
sudo pip3 install -U cp2stdout
```

## Usage

Update config.yml and run

```sh
cp2stdout -c config.yml
```

### PM2
```sh
pm2 start `which python3` --name "cp2stdout" -- `which cp2stdout` -c /etc/cooper/cp2stdout.yml
```

## License

This project is licensed under the [**MIT License**](https://opensource.org/licenses/MIT/) - see the [**LICENSE**](LICENSE) file for details.
