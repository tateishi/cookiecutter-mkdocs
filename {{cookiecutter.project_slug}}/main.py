def define_env(env):
    @env.macro
    def hello():
        return f"Hello World."
        
