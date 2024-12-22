import torch
import platform
import os

class Environment:
    @staticmethod
    def get_device():
        return torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    
    @staticmethod
    def is_notebook():
        try:
            from IPython import get_ipython
            if 'google.colab' in str(get_ipython()):
                return True, 'colab'
            return True, 'jupyter'
        except:
            return False, 'desktop'
    
    @staticmethod
    def get_requirements():
        cpu_only = not torch.cuda.is_available()
        return {
            'pytorch': f"torch {'cpu' if cpu_only else 'cuda'} version {torch.__version__}",
            'system': platform.system(),
            'python': platform.python_version()
        }