namespace Tioring_mashine;
using System;
using System.Drawing;
using System.Drawing.Drawing2D;
using System.Windows.Forms;
using System.IO;
using System.Runtime.InteropServices;
using System.Diagnostics;

public partial class Form1 : Form
{
    public Form1()
    {
        InitializeComponent();
    }
        Form load;
        Form safe;
        Button loader;
        Button saver;
        TextBox saving_project_name_value;
        TextBox loading_project_name_value;
        TextBox loading_error;
        TextBox saving_error;
        Form problem;

        private void save_continue_Click(object sender, System.EventArgs e) {
            string project_name = saving_project_name_value.Text;
            Save_project(project_name);
            safe.Dispose(); 
        }

        private void load_continue_Click(object sender, System.EventArgs e) {
            string project_name = loading_project_name_value.Text;
            if(!(File.Exists("Project_storage/" + project_name + ".txt")) ) {
                loading_error.Visible = true;
            }
            else {
                Load_project(project_name);
                load.Dispose();
            }
        }
        private void safe_Click(object sender,EventArgs e) {
            if (safe != null) {
                safe.Dispose();
            }
            safe=new Form();
            safe.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            safe.ClientSize = new System.Drawing.Size(400, 130);
            safe.Text = "Сохранение";
            safe.MaximumSize = new System.Drawing.Size(400, 180);
            safe.MinimumSize = new System.Drawing.Size(400, 180);
            safe.MaximizeBox = false;
            safe.BackColor = System.Drawing.Color.DarkGoldenrod;
            safe.Show();

            saver = new Button();
            saver.Text = "Continue";
            saver.Location = new Point(150, 70);
            saver.Size = new Size(80,56);
            saver.BackColor = Color.BurlyWood;
            safe.Controls.Add(saver);

            saving_project_name_value = new TextBox();
            saving_project_name_value.Location = new Point(35, 10);
            saving_project_name_value.Size = new Size(325, 90);
            saving_project_name_value.Text = "Имя_проекта";
            saving_project_name_value.BackColor = Color.OrangeRed;
            saving_project_name_value.ForeColor = Color.White;
            safe.Controls.Add(saving_project_name_value);

            saving_error = new TextBox();
            saving_error.Location = new Point(90, 40);
            saving_error.Size = new Size(225,90);
            saving_error.Text = "Пустой проект!";
            saving_error.BackColor = Color.Red;
            saving_error.Enabled = false;
            saving_error.Visible = false;
            safe.Controls.Add(saving_error);

            saver.Click += new EventHandler(save_continue_Click);
        }

        private void load_Click(object sender,EventArgs e) {
            if (load != null) {
                load.Dispose();
            }
            load=new Form();
            load.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            load.ClientSize = new System.Drawing.Size(400, 130);
            load.Text = "Загрузка";
            load.MaximumSize = new System.Drawing.Size(400, 180);
            load.MinimumSize = new System.Drawing.Size(400, 180);
            load.MaximizeBox = false;
            load.BackColor = System.Drawing.Color.DarkGoldenrod;
            load.Show();

            loader = new Button();
            loader.Text = "Continue";
            loader.Location = new Point(150, 70);
            loader.Size = new Size(80,56);
            loader.BackColor = Color.BurlyWood;
            load.Controls.Add(loader);

            loading_project_name_value = new TextBox();
            loading_project_name_value.Location = new Point(35, 10);
            loading_project_name_value.Size = new Size(325,90);
            loading_project_name_value.Text = "Имя_проекта";
            loading_project_name_value.BackColor = Color.OrangeRed;
            loading_project_name_value.ForeColor = Color.White;
            load.Controls.Add(loading_project_name_value);

            loading_error = new TextBox();
            loading_error.Location = new Point(90, 40);
            loading_error.Size = new Size(225,90);
            loading_error.Text = "Несуществующий проект!";
            loading_error.BackColor = Color.Red;
            loading_error.Enabled = false;
            loading_error.Visible = false;
            load.Controls.Add(loading_error);

            loader.Click += new EventHandler(load_continue_Click);
        }
    private void play_Click(object sender,EventArgs e) {
        string[] lines = code.Text.Split('\n');
        if (lines[0].Split(' ').Length == 2) {
            Process p = new Process();
            p.StartInfo.UseShellExecute = false;
            p.StartInfo.Arguments = "interpreter.py";
            // Перехватываем вывод
            p.StartInfo.RedirectStandardOutput = true;
            p.StartInfo.RedirectStandardInput = true;
            p.StartInfo.CreateNoWindow = true;
            // Запускаемое приложение
            p.StartInfo.FileName = "python";
            //p.StartInfo.FileName = "example.exe";

            // Передаем необходимые аргументы
            // p.Arguments = "example.txt";
            p.Start();
            // Результат работы консольного приложения
            p.StandardInput.WriteLine(this.Text);
            p.StandardInput.WriteLine(code.Text);
            // Дождаться завершения запущенного приложения
            p.WaitForExit();
        }
        else {
            Process p = new Process();
            p.StartInfo.UseShellExecute = false;
            p.StartInfo.Arguments = "ui.py";
            // Перехватываем вывод
            p.StartInfo.RedirectStandardOutput = true;
            p.StartInfo.RedirectStandardInput = true;
            p.StartInfo.CreateNoWindow = true;
            // Запускаемое приложение
            p.StartInfo.FileName = "python";
            //p.StartInfo.FileName = "example.exe";

            // Передаем необходимые аргументы
            // p.Arguments = "example.txt";
            p.Start();
            // Результат работы консольного приложения
            p.StandardInput.WriteLine(code.Text+"\nend");
            // Дождаться завершения запущенного приложения
            p.WaitForExit();
        }
    }
    void Save_project(string project_name) {
        project_name_change(project_name);
        Directory.CreateDirectory(Path.Combine(Directory.GetCurrentDirectory(), "Project_storage"));
        File.WriteAllText(Path.Combine(Directory.GetCurrentDirectory(), "Project_storage", project_name + ".txt"), code.Text);
    }

    void Load_project(string project_name) {
        project_name_change(project_name);
        code.Text = File.ReadAllText("Project_storage/" + project_name + ".txt");
        this.Invalidate();    
    }
}
