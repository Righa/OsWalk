import os

dwalk = os.walk('D:\\.111\\python')

# directories to exclude

edirs = [
	'D:\\.111\\python\\oukrekya\\.git\\',
	'D:\\.111\\python\\oukrekya\\',
	'D:\\.111\\python\\pyautogui\\'
]

# main

def main():
	for root, dirs, files in dwalk:
		#os.system('cmd /k "Your Command Prompt Command"')
		for file in files:
			if not e_dir(root):
				print(root+'\\'+file)
# exclude directories

def e_dir(mdr):
	for dr in edirs:
		if mdr.startswith(dr):
			return True
	return False


# run main after loading all funcs

if __name__ == '__main__':
	print(__name__)
	main()
