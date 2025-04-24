import tkinter as tk
import time
from tkinter import ttk, scrolledtext

class StopwatchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cronómetro")
        self.root.geometry("500x400")
        self.root.resizable(False, False)
        
        # Configuración de colores y estilos
        self.root.configure(bg="#f0f0f0")
        self.style = ttk.Style()
        self.style.configure("TButton", font=("Arial", 10))
        self.style.configure("TFrame", background="#f0f0f0")
        
        # Variables para el cronómetro
        self.start_time = None
        self.running = False
        self.elapsed = 0
        self.laps = []
        self.lap_count = 0
        self.update_id = None
        
        # Crear widgets
        self.create_widgets()
        
    def create_widgets(self):
        # Marco principal
        main_frame = ttk.Frame(self.root, padding=10)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Pantalla del cronómetro
        self.time_display = tk.Label(
            main_frame,
            text="00:00:00.000",
            font=("Arial", 36, "bold"),
            bg="#ffffff",
            fg="#333333",
            relief=tk.RAISED,
            bd=2,
            padx=20,
            pady=10
        )
        self.time_display.pack(pady=20, fill=tk.X)
        
        # Marco para botones
        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack(pady=10)
        
        # Botones
        self.start_btn = ttk.Button(
            btn_frame,
            text="Iniciar",
            width=12,
            command=self.toggle_start_stop
        )
        self.start_btn.grid(row=0, column=0, padx=5, pady=5)
        
        self.reset_btn = ttk.Button(
            btn_frame,
            text="Reiniciar",
            width=12,
            command=self.reset
        )
        self.reset_btn.grid(row=0, column=1, padx=5, pady=5)
        
        self.lap_btn = ttk.Button(
            btn_frame,
            text="Vuelta",
            width=12,
            command=self.lap
        )
        self.lap_btn.grid(row=0, column=2, padx=5, pady=5)
        
        self.clear_laps_btn = ttk.Button(
            btn_frame,
            text="Limpiar Vueltas",
            width=12,
            command=self.clear_laps
        )
        self.clear_laps_btn.grid(row=0, column=3, padx=5, pady=5)
        
        # Área de vueltas
        laps_frame = ttk.LabelFrame(main_frame, text="Vueltas", padding=10)
        laps_frame.pack(pady=10, fill=tk.BOTH, expand=True)
        
        self.laps_area = scrolledtext.ScrolledText(
            laps_frame,
            width=40,
            height=8,
            font=("Arial", 10),
            state="disabled"
        )
        self.laps_area.pack(fill=tk.BOTH, expand=True)
        
        # Etiqueta de estado
        self.status_label = tk.Label(
            main_frame,
            text="Listo para comenzar",
            font=("Arial", 8),
            bg="#f0f0f0",
            fg="#666666"
        )
        self.status_label.pack(pady=5, anchor=tk.SE)
    
    def toggle_start_stop(self):
        if not self.running:
            self.start()
        else:
            self.stop()
    
    def start(self):
        """Inicia o reanuda el cronómetro."""
        if not self.running:
            self.running = True
            self.start_time = time.time() - self.elapsed
            self.start_btn.config(text="Detener")
            self.status_label.config(text="Cronómetro en funcionamiento")
            self.update_display()
    
    def stop(self):
        """Detiene el cronómetro."""
        if self.running:
            self.running = False
            self.elapsed = time.time() - self.start_time
            self.start_btn.config(text="Reanudar")
            self.status_label.config(text=f"Detenido en {self.format_time(self.elapsed)}")
            if self.update_id:
                self.root.after_cancel(self.update_id)
                self.update_id = None
    
    def reset(self):
        """Reinicia el cronómetro a cero."""
        self.stop()
        self.elapsed = 0
        self.start_time = None
        self.start_btn.config(text="Iniciar")
        self.time_display.config(text="00:00:00.000")
        self.status_label.config(text="Cronómetro reiniciado")
    
    def lap(self):
        """Registra una vuelta."""
        if self.running:
            current_time = time.time() - self.start_time
            self.lap_count += 1
            self.laps.append(current_time)
            
            # Calcular intervalo desde la última vuelta
            interval = current_time
            if len(self.laps) > 1:
                interval = current_time - self.laps[-2]
            
            # Añadir a la visualización
            self.laps_area.config(state="normal")
            self.laps_area.insert(
                tk.END, 
                f"Vuelta {self.lap_count}: {self.format_time(current_time)} (Intervalo: {self.format_time(interval)})\n"
            )
            self.laps_area.see(tk.END)
            self.laps_area.config(state="disabled")
            
            self.status_label.config(text=f"Vuelta {self.lap_count} registrada")
    
    def clear_laps(self):
        """Limpia el registro de vueltas."""
        self.laps = []
        self.lap_count = 0
        self.laps_area.config(state="normal")
        self.laps_area.delete(1.0, tk.END)
        self.laps_area.config(state="disabled")
        self.status_label.config(text="Registro de vueltas limpiado")
    
    def update_display(self):
        """Actualiza la pantalla con el tiempo actual."""
        if self.running:
            current_time = time.time() - self.start_time
            self.time_display.config(text=self.format_time(current_time))
            self.update_id = self.root.after(10, self.update_display)  # Actualiza cada 10ms
    
    def format_time(self, seconds):
        """Formatea el tiempo en horas:minutos:segundos.milisegundos."""
        milliseconds = int((seconds % 1) * 1000)
        seconds = int(seconds)
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}.{milliseconds:03d}"

def main():
    root = tk.Tk()
    app = StopwatchApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()