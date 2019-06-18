import os
import subprocess


def run(cmd):
    cmd = ('argocd ' + cmd).split()
    output = subprocess.check_output(cmd)
    return output.decode('utf-8')


def login():
    host = 'localhost:8080'
    password = os.environ['ARGOCD_PASSWORD']
    cmd = f'login {host} --insecure --username admin --password {password}'
    output = run(cmd)
    print(output)


def get_apps(namespace):
    """ """
    output = run(f'app list -o wide')
    keys = 'name project namespace path repo'.split()
    apps = []
    lines = output.split('\n')
    headers = [h.lower() for h in lines[0].split()]
    for line in lines[1:]:
        items = line.split()
        app = {k: v for k, v in zip(headers, items) if k in keys}
        if app:
            apps.append(app)
    return apps


def create_project(project, cluster, namespace, description, repo):
    """ """
    cmd = f'proj create {project} --description {description} -d {cluster},{namespace} -s {repo}'
    output = run(cmd)
    print(output)

    # Add access to resources
    cmd = f'proj allow-cluster-resource {project} "*" "*"'
    output = run(cmd)
    print(output)


def create_app(name, project, namespace, repo, path):
    """ """
    cmd = f"""app create {name} --project {project} --dest-server https://kubernetes.default.svc 
              --dest-namespace {namespace} --repo {repo} --path {path}"""
    output = run(cmd)
    print(output)


def main():
    login()
    project = 'default'
    ns = 'default'
    description = 'Delicious-like link management system'
    repo = 'https://github.com/the-gigi/delinkcious'
    # create_project(project, 'https://kubernetes.default.svc', ns, '', repo)
    for app in 'link social-graph user news api-gateway'.split():
        service = app.replace('-', '_') + '_service'
        create_app(app, project, ns, repo, f'svc/{service}/k8s')


if __name__ == '__main__':
    main()
