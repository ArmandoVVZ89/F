import os
import subprocess

# Definición de rutas y configuraciones
PROJECT_PATH = os.path.join(os.getcwd(), "MEDIO")
BUILD_GRADLE_PATH = os.path.join(PROJECT_PATH, "app/build.gradle")
MANIFEST_PATH = os.path.join(PROJECT_PATH, "app/src/main/AndroidManifest.xml")
SETTINGS_GRADLE_PATH = os.path.join(PROJECT_PATH, "settings.gradle")
GRADLE_PROPERTIES_PATH = os.path.join(PROJECT_PATH, "gradle.properties")
OUTPUT_LOG_PATH = os.path.join(PROJECT_PATH, "supervision_log.txt")

# Función de supervisión y generación
def supervisar_y_generar():
    print("Iniciando supervisión del proyecto...")
    errores = []

    if not os.path.exists(BUILD_GRADLE_PATH):
        errores.append("Falta build.gradle. Se generará automáticamente.")
        generar_build_gradle(complejidad='complejo')

    if not os.path.exists(MANIFEST_PATH):
        errores.append("Falta AndroidManifest.xml. Se generará automáticamente.")
        generar_manifest(complejidad='complejo')

    if not os.path.exists(SETTINGS_GRADLE_PATH):
        errores.append("Falta settings.gradle. Se generará automáticamente.")
        generar_settings_gradle()

    if not os.path.exists(GRADLE_PROPERTIES_PATH):
        errores.append("Falta gradle.properties. Se generará automáticamente.")
        generar_gradle_properties()

    if errores:
        print("Errores detectados y archivos generados:")
        print("\n".join(errores))
    else:
        print("Todos los archivos están en su lugar.")

# Funciones para generar archivos específicos
def generar_build_gradle(complejidad='simple'):
    print("Generando build.gradle...")
    with open(BUILD_GRADLE_PATH, 'w') as f:
        f.write("// Archivo build.gradle generado automáticamente\n")
        f.write("apply plugin: 'com.android.application'\n")
        if complejidad == 'complejo':
            f.write("android {\n")
            f.write("    compileSdkVersion 30\n")
            f.write("    defaultConfig {\n")
            f.write("        applicationId \"com.example.app\"\n")
            f.write("        minSdkVersion 21\n")
            f.write("        targetSdkVersion 30\n")
            f.write("        versionCode 1\n")
            f.write("        versionName \"1.0\"\n")
            f.write("    }\n")
            f.write("    buildTypes {\n")
            f.write("        release {\n")
            f.write("            minifyEnabled false\n")
            f.write("            proguardFiles getDefaultProguardFile('proguard-android-optimize.txt'), 'proguard-rules.pro'\n")
            f.write("        }\n")
            f.write("    }\n")
            f.write("}\n")
            f.write("dependencies {\n")
            f.write("    implementation 'androidx.appcompat:appcompat:1.2.0'\n")
            f.write("}\n")
        else:
            f.write("android { compileSdkVersion 30 }\n")
    print("build.gradle generado.")

def generar_manifest(complejidad='simple'):
    print("Generando AndroidManifest.xml...")
    with open(MANIFEST_PATH, 'w') as f:
        f.write('<?xml version="1.0" encoding="utf-8"?>\n')
        f.write('<manifest xmlns:android="http://schemas.android.com/apk/res/android" package="com.example.app">\n')
        f.write('    <application>\n')
        if complejidad == 'complejo':
            f.write('        <activity android:name=".MainActivity">\n')
            f.write('            <intent-filter>\n')
            f.write('                <action android:name="android.intent.action.MAIN" />\n')
            f.write('                <category android:name="android.intent.category.LAUNCHER" />\n')
            f.write('            </intent-filter>\n')
            f.write('        </activity>\n')
            f.write('        <activity android:name=".SettingsActivity" />\n')
        else:
            f.write('        <activity android:name=".MainActivity">\n')
            f.write('            <intent-filter>\n')
            f.write('                <action android:name="android.intent.action.MAIN" />\n')
            f.write('                <category android:name="android.intent.category.LAUNCHER" />\n')
            f.write('            </intent-filter>\n')
            f.write('        </activity>\n')
        f.write('    </application>\n')
        f.write('</manifest>\n')
    print("AndroidManifest.xml generado.")

def generar_settings_gradle():
    print("Generando settings.gradle...")
    with open(SETTINGS_GRADLE_PATH, 'w') as f:
        f.write("// Archivo settings.gradle generado automáticamente\n")
        f.write("include ':app'\n")
    print("settings.gradle generado.")

def generar_gradle_properties():
    print("Generando gradle.properties...")
    with open(GRADLE_PROPERTIES_PATH, 'w') as f:
        f.write("# Archivo gradle.properties generado automáticamente\n")
        f.write("org.gradle.jvmargs=-Xmx1536m\n")
    print("gradle.properties generado.")

# Función para invocar el script de corrección
def ejecutar_correcciones():
    print("Ejecutando correcciones en el proyecto...")
    comando = f"python3 {os.path.join(os.getcwd(), 'script_resuelve_2.py')}"
    try:
        resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
        print("Correcciones realizadas:\n", resultado.stdout)
        if resultado.stderr:
            print("Errores durante la corrección:\n", resultado.stderr)
    except subprocess.CalledProcessError as e:
        print("Error al ejecutar script_resuelve_2.py:", e.stderr)

# Función para generar un informe de ejecución
def generar_informe():
    with open(OUTPUT_LOG_PATH, 'w') as log:
        log.write("Informe de supervisión y corrección del proyecto\n\n")
        log.write("Archivos generados:\n")
        log.write("  - build.gradle\n")
        log.write("  - AndroidManifest.xml\n")
        log.write("  - settings.gradle\n")
        log.write("  - gradle.properties\n")
        log.write("\nRevisiones realizadas:\n")
        log.write("Se ejecutó el script de correcciones y se capturaron las salidas.\n")
    print("Informe generado en", OUTPUT_LOG_PATH)

# Función principal
def main():
    # Supervisar y generar archivos básicos
    supervisar_y_generar()

    # Ejecutar el script de correcciones
    ejecutar_correcciones()

    # Generar un informe de ejecución
    generar_informe()

    print("Proceso de supervisión, generación y corrección completado.")

# Ejecutar la función principal
if __name__ == "__main__":
    main()