from setuptools import setup, find_packages

setup(
    name='jupyterhub-kubespawner',
    version='0.8.1',
    install_requires=[
        'jupyterhub>=0.8',
        'pyYAML',
        'kubernetes==4.*',
        'escapism',
        'jinja2',
        'async_generator>=1.8',
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    description='JupyterHub Spawner targeting Kubernetes',
    url='http://github.com/jupyterhub/kubespawner',
    author='Yuvi Panda',
    author_email='yuvipanda@gmail.com',
    license='BSD',
    packages=find_packages(),
)
