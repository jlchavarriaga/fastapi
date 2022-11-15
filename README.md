# Fastapi

**Guia Basica** _desde cero_ para implementar un proyecto con fastapi
**_Primero lo primero_**, empezaremos desde actualizar PIP, hasta implementar autenticacion

 ###### PASO A PASO
<ol> 
   <li> ACTUALIZAR PIP</li>
      <code> pip install --upgrade pip </code>
   <li> ENTORNO VIRTUAL 
      <ol>
      <li> <code> pip install virtualenv </code> </li>
      <li> <code> python3 -m virtualenv venv </code> creamos el entorno virtual</li>
      <li> <code> source venv/bin/activate </code> activamos el entorno virtual</li>
      <li><code> deactivate </code> para desactivar el entorno virtual</li>
      </ol>
   </li>
   <li>INSTALACION
      <BLOCKQUOTE>  
         <p>incluyendo algunas dependencias necesarias como uvicorn</p> 
      </BLOCKQUOTE>
      <ol>
         <li> ejecutamos en consola <code> python -m pip install "fastapi[all]" </code></li>
      </ol>
   </li>
   <li>EJECUCION
      <code>uvicorn carsharing:app --reload</code>
      <blockquote>
         <p> uvicorn es un http server   </p>
         <p>carsharing es el nombre del archivo de python que contiene el objeto de la aplicacion
         </p>
         <p>app es el nombre del objeto de la aplicacion que tiene el archivo</p>
      </blockquote>
   </li>
    <li>CODIGO
      <blockquote>
        <p> 
        <code>    
        from fastapi import FastAPI
        </code>
        <p> 
        <code>
         app = FastAPI()
        </code>
    </p> 
    <p> 
    #el objeto resultante, que representa nuestra aplicacion o
    en otras palabras el REST service que construimos es guardada en una variable llamada app
   </p>
      </blockquote>
    <blockquote>
    <p>
    <code>   
    @app.get("/date")<p>
    def date():<p>
        """Return a friendly welcome message."""</p>
        return {'date':datetime.now()}</code>
    <p> aplicar la asignacion de la URL a la funcion definida debajo de ella</p>
    <p>app get es un tipo de funcion que permite argumentos</p>
    </p>
    </blockquote>
    </li>
    <li>DOCUMENTACION
      <blockquote>
        <p> /docs </p>
        <p> /redoc </p>
      </blockquote>
    </li>
    <li>NOTAS
      <blockquote>
        <p> el flujo de una aplicacion en fast api , esta determinado por las solicitudes http que ingresan </p>
      </blockquote>
    </li>
</ol>

