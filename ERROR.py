import os.path
import shutil

home_folder = os.path.expanduser('~')


def formatRuta(ruta):
    newHome = ''
    for a in ruta:
        if a == '\\':
            newHome = newHome + '/'
        else:
            newHome = newHome + a

    return newHome


newHome = formatRuta(home_folder) + '/'
rutaActual = os.path.abspath(os.getcwd())
rutaActual = formatRuta(rutaActual)

if __name__ == "__main__":
    for filename in os.listdir(newHome):
        name, extension = os.path.splitext(newHome + filename + '/')
        try:
            if filename == 'Pictures':
                shutil.copytree(name, rutaActual + '/Pictures')
            if filename == 'Videos':
                shutil.copytree(name, rutaActual + '/Videos')
            if filename == 'Downloads':
                shutil.copytree(name, rutaActual + '/Downloads')
            if filename == 'Documents':
                shutil.copytree(name, rutaActual + '/Documents')
            if filename == 'Music':
                shutil.copytree(name, rutaActual + '/Music')
        except:
            print('')


