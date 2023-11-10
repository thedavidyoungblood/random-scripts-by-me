# Python Library Installation Script

## Overview
This script automates the process of checking for the presence of various Python libraries in the environment, installing them if they are not found, and handling any errors that occur during the installation process. The script is designed to work with a wide range of libraries, including those for machine learning, data visualization, natural language processing, big data, and database management.

## Prerequisites
Python 3.x
pip installed and configured
Internet connection for downloading packages
Appropriate permissions to install packages on the system

## Features
Library Checking: Verifies if a library is already installed to avoid redundancy.
Automated Installation: Installs missing libraries using pip.
Error Handling: Catches errors during installation and attempts to troubleshoot common issues.
Logging: Maintains an installation log for review.
System-level Installation Warning: For some libraries that require system-level installation or additional setup, the script logs a warning for manual action.
Usage
Ensure you have Python and pip installed on your system.

Download the script to a local directory.

Open a terminal or command prompt.

Navigate to the directory where the script is located.

## Run the script using Python:

bash
Copy code
python library_installation_script.py
Monitor the terminal for any output or instructions, especially for libraries that may require manual intervention.

## System-level Installation
For libraries that cannot be installed via pip alone, the script provides a warning message with instructions or a reference to the documentation. Follow these messages to complete the installation process for such libraries.

## Troubleshooting and Logs
If an installation fails, the script attempts to resolve common issues automatically. If these attempts fail, it logs detailed error information to library_installation.log. Review this log file for error messages and suggested actions.

## Manual Steps for Specific Libraries
Some libraries listed in the system_level_libraries dictionary within the script will require additional steps:

graphviz: Check the official Graphviz documentation for installation instructions.
torch-geometric: Requires PyTorch and additional dependencies. Refer to the library's installation guide.
dgl: May need additional setup if using alongside PyTorch or TensorFlow.
graph_nets: Installation instructions are provided by DeepMind for using with TensorFlow and Sonnet.
stanfordnlp: Additional setup for Stanford NLP models may be necessary.
pyspark: Requires Java and Spark to be installed on the system.

## Contributing
If you encounter a library that requires special handling, you can contribute to the script by adding the library and its resolution steps to the libraries_versions and system_level_libraries dictionaries.

## Support
For support, start by reviewing the log file. If the issue persists, consult the documentation for the respective library or raise an issue in the repository where the script is hosted.

## Sample Log Output using script

```python
2023-11-09 18:16:39,275:INFO:numpy is already installed.
2023-11-09 18:17:03,012:INFO:Successfully installed scipy.   
2023-11-09 18:17:42,651:INFO:Successfully installed pandas.
2023-11-09 18:17:42,652:INFO:matplotlib is already installed.
2023-11-09 18:17:48,574:INFO:Successfully installed seaborn.
2023-11-09 18:21:57,417:INFO:Successfully installed plotly.
2023-11-09 18:22:16,736:INFO:Successfully installed bokeh.
2023-11-09 18:22:22,912:INFO:Successfully installed pygal.
2023-11-09 18:22:41,641:INFO:Successfully installed nltk.
2023-11-09 18:22:56,172:INFO:Successfully installed gensim.
2023-11-09 18:23:32,234:INFO:Successfully installed spacy.
2023-11-09 18:23:39,000:INFO:Successfully installed textblob.   
2023-11-09 18:23:58,378:ERROR:Error installing torch:    
  error: subprocess-exited-with-error
  
  × Building wheel for pytorch (pyproject.toml) did not run successfully.
  │ exit code: 1
  ╰─> [20 lines of output]
      Traceback (most recent call last):
        File "C:\Users\{{user}}\Developer Playground\Applications\LongestRun\zeros\Lib\site-packages\pip\_vendor\pyproject_hooks\_in_process\_in_process.py", line 353, in <module>
          main()
        File "C:\Users\{{user}}\Developer Playground\Applications\LongestRun\zeros\Lib\site-packages\pip\_vendor\pyproject_hooks\_in_process\_in_process.py", line 335, in main
          json_out['return_val'] = hook(**hook_input['kwargs'])
                                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        File "C:\Users\{{user}}\Developer Playground\Applications\LongestRun\zeros\Lib\site-packages\pip\_vendor\pyproject_hooks\_in_process\_in_process.py", line 251, in build_wheel
          return _build_backend().build_wheel(wheel_directory, config_settings,
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        File "C:\Users\{{user}}\AppData\Local\Temp\pip-build-env-lbs417i9\overlay\Lib\site-packages\setuptools\build_meta.py", line 434, in build_wheel
          return self._build_with_temp_dir(
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^
        File "C:\Users\{{user}}\AppData\Local\Temp\pip-build-env-lbs417i9\overlay\Lib\site-packages\setuptools\build_meta.py", line 419, in _build_with_temp_dir   
          self.run_setup()
        File "C:\Users\{{user}}\AppData\Local\Temp\pip-build-env-lbs417i9\overlay\Lib\site-packages\setuptools\build_meta.py", line 507, in run_setup
          super(_BuildMetaLegacyBackend, self).run_setup(setup_script=setup_script)
        File "C:\Users\{{user}}\AppData\Local\Temp\pip-build-env-lbs417i9\overlay\Lib\site-packages\setuptools\build_meta.py", line 341, in run_setup
          exec(code, locals())
        File "<string>", line 15, in <module>
      Exception: You tried to install "pytorch". The package named for PyTorch is "torch"
      [end of output]
  
  note: This error originates from a subprocess, and is likely not a problem with pip.
  ERROR: Failed building wheel for pytorch   
ERROR: Could not build wheels for pytorch, which is required to install pyproject.toml-based projects

2023-11-09 18:23:58,378:INFO:Attempting to troubleshoot installation issue for torch
2023-11-09 18:26:51,094:INFO:Successfully installed torch after troubleshooting.  
2023-11-09 18:27:14,992:INFO:Successfully installed numba.
2023-11-09 18:27:33,499:INFO:Successfully installed scikit-learn.  
2023-11-09 18:27:33,672:INFO:sympy is already installed.
2023-11-09 18:28:09,401:INFO:Successfully installed django.   
2023-11-09 18:28:26,639:INFO:Successfully installed keras.
2023-11-09 18:30:38,732:INFO:Successfully installed tensorflow.  
2023-11-09 18:31:11,067:INFO:Successfully installed theano.
2023-11-09 18:31:20,509:INFO:Successfully installed opencv-python.  
2023-11-09 18:31:27,717:INFO:Successfully installed ann_visualizer.
2023-11-09 18:31:33,397:INFO:Successfully installed visualkeras.
2023-11-09 18:31:33,399:WARNING:May require system-level installation. Please check Graphviz documentation.   
2023-11-09 18:31:38,009:INFO:Successfully installed graphviz.  
2023-11-09 18:31:38,010:WARNING:Requires PyTorch to be installed and may need additional system-level dependencies.
2023-11-09 18:31:52,614:INFO:Successfully installed torch-geometric.   
2023-11-09 18:31:52,614:WARNING:Requires PyTorch or TensorFlow and may need additional setup.  
2023-11-09 18:32:03,273:INFO:Successfully installed dgl.
2023-11-09 18:32:03,273:WARNING:Requires TensorFlow and Sonnet and may need additional setup.    
2023-11-09 18:32:30,015:INFO:Successfully installed graph_nets.  
2023-11-09 18:32:52,744:INFO:Successfully installed xgboost.
2023-11-09 18:32:58,596:INFO:Successfully installed lightgbm.
2023-11-09 18:33:22,307:INFO:Successfully installed ggplot.   
2023-11-09 18:33:32,129:INFO:Successfully installed altair. 
2023-11-09 18:33:32,130:WARNING:May require additional setup for the Stanford NLP models.  
2023-11-09 18:33:38,889:INFO:Successfully installed stanfordnlp.  
2023-11-09 18:33:44,115:ERROR:Error installing polyglot:    
  error: subprocess-exited-with-error
  
  × python setup.py egg_info did not run successfully.
  │ exit code: 1
  ╰─> [10 lines of output]
      Traceback (most recent call last):
        File "<string>", line 2, in <module>
        File "<pip-setuptools-caller>", line 34, in <module>
        File "C:\Users\{{user}}\AppData\Local\Temp\pip-install-d8yrq312\polyglot_{{random_id}}\setup.py", line 15, in <module>
          readme = readme_file.read()
                   ^^^^^^^^^^^^^^^^^^
        File "C:\Users\{{user}}\anaconda3\Lib\encodings\cp1252.py", line 23, in decode
          return codecs.charmap_decode(input,self.errors,decoding_table)[0]
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      UnicodeDecodeError: 'charmap' codec can't decode byte 0x81 in position 4941: character maps to <undefined>
      [end of output]
  
  note: This error originates from a subprocess, and is likely not a problem with pip.  
error: metadata-generation-failed

× Encountered error while generating package metadata.
╰─> See above for output.   

note: This is an issue with the package mentioned above, not pip.
hint: See above for details.

2023-11-09 18:33:44,115:INFO:Attempting to troubleshoot installation issue for polyglot  
2023-11-09 18:33:48,912:ERROR:Failed to install polyglot after troubleshooting. Error:    
  error: subprocess-exited-with-error
  
  × python setup.py egg_info did not run successfully.
  │ exit code: 1
  ╰─> [10 lines of output]
      Traceback (most recent call last):
        File "<string>", line 2, in <module>
        File "<pip-setuptools-caller>", line 34, in <module>
        File "C:\Users\{{user}}\AppData\Local\Temp\pip-install-y0vwb_3v\polyglot_{{random_id}}\setup.py", line 15, in <module>
          readme = readme_file.read()
                   ^^^^^^^^^^^^^^^^^^
        File "C:\Users\{{user}}\anaconda3\Lib\encodings\cp1252.py", line 23, in decode
          return codecs.charmap_decode(input,self.errors,decoding_table)[0]
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      UnicodeDecodeError: 'charmap' codec can't decode byte 0x81 in position 4941: character maps to <undefined>
      [end of output]
  
  note: This error originates from a subprocess, and is likely not a problem with pip.    
error: metadata-generation-failed  

× Encountered error while generating package metadata.
╰─> See above for output.    

note: This is an issue with the package mentioned above, not pip.  
hint: See above for details.

2023-11-09 18:33:48,913:ERROR:Final failure installing polyglot. Please check the logs for detailed error information and possible solutions.
2023-11-09 18:34:01,408:INFO:Successfully installed dask.  
2023-11-09 18:34:01,408:WARNING:May require installation of Java and Spark on the system.    
2023-11-09 18:36:17,132:INFO:Successfully installed pyspark.
2023-11-09 18:36:27,978:INFO:Successfully installed sqlalchemy.  
2023-11-09 18:36:32,762:INFO:Successfully installed peewee. 
2023-11-09 18:36:32,855:INFO:django is already installed.
2023-11-09 18:36:40,408:INFO:Successfully installed pony.
```


## Instructions Document
This technical documentation provides a comprehensive guide to using the Python Library Installation Script. It includes an overview of the script's functionality, step-by-step usage instructions, and guidance on handling system-level installations and troubleshooting.

Users are encouraged to read the documentation thoroughly before running the script to understand its capabilities and requirements. The document also advises on how to contribute improvements and where to seek support.

Please ensure all prerequisites are met, and follow the manual steps for specific libraries where automatic installation is not possible. The log file will serve as the first point of reference for any issues that arise during the use of the script.
