import importlib.util
import sys
import os

TEST_PATH = os.path.join(os.getcwd(), r"RE_E2E_testScripts\R8S3\test_r8_patch2_ddl copy.py")
print(f"Loading test module from: {TEST_PATH}")

spec = importlib.util.spec_from_file_location("test_mod", TEST_PATH)
mod = importlib.util.module_from_spec(spec)
# Ensure workspace root is on sys.path for relative imports
sys.path.insert(0, os.getcwd())

try:
    spec.loader.exec_module(mod)
    print("Module loaded.")
    if hasattr(mod, 'Test_ddl_v3'):
        test_obj = mod.Test_ddl_v3()
        print("Instantiated Test_ddl_v3, running test method...")
        print("Available attributes:", [a for a in dir(test_obj) if not a.startswith("__")])
        # attempt to find matching test method by prefix
        method_name = None
        for attr in dir(test_obj):
            if attr.startswith('test1_positive'):
                method_name = attr
                break
        if method_name:
            try:
                print(f"Calling method: {method_name}")
                getattr(test_obj, method_name)()
                print("Test method finished.")
            except Exception as e:
                print(f"Test method raised exception: {e}")
        else:
            print("No matching test method found on Test_ddl_v3 instance.")
    else:
        print("Test_ddl_v3 class not found in module.")
except Exception as e:
    print(f"Failed to load/execute module: {e}")
