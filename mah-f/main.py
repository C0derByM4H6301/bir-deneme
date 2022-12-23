import cmd
import importlib
import sys

class MyPrompt(cmd.Cmd):
    def do_use(self, module_path):
        """
        Modülü kullanmaya başlar.
        
        Kullanım: use [modül yolu]
        """
        self.module = importlib.import_module(module_path)
        self.prompt = "mah-f ({})> ".format(module_path)

    def complete_use(self, text, line, start_index, end_index):
        """
        "use" komutu için otomatik tamamlama.
        """
        return [
            path for path in self.module_paths
            if path.startswith(text)
        ]

    def do_set(self, line):
        """
        Modüldeki bir değişkeni değiştirir.
        
        Kullanım: set [değişken adı] [değer]
        """
        variable, value = line.split()
        self.module.__dict__[variable] = value

    def do_run(self, line):
        """
        Modülü çalıştırır.
        
        Kullanım: run
        """
        self.module.main()

    def do_execute(self, line):
        """
        Modülü çalıştırır.
        
        Kullanım: execute
        """
        self.module.main()
        
    def do_exit(self, line):
        """
        Programdan çıkış yapar.
        
        Kullanım: exit
        """
        return True
    
    def do_show(self, line):
        """
        Modülleri veya modül seçeneklerini gösterir.
        
        Kullanım: show modules | show options
        """
        if line == "modules":
            print("Import edilebilir modüller:")
            for path in self.module_paths:
                print(" - {}".format(path))
        elif line == "options":
            if not hasattr(self, "module"):
                print("Lütfen önce bir modül seçin!")
            else:
                print("Modül seçenekleri:")
                for name, value in self.module.__dict__.items():
                    print(" - {}: {}".format(name, value))
        else:
            print("Geçersiz komut! Lütfen 'modules' veya 'options' yazın.")

if __name__ == "__main__":
    sys.path.append("modules")
    prompt = MyPrompt()
    prompt.module_paths = ["modules/ping", "modules/echo"]
    prompt.prompt = "mah-f>"
    prompt.cmdloop()
