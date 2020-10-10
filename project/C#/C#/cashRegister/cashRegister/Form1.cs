using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace cashRegister
{
    
    public partial class Form1 : Form
    {
        double totalPrice = 0.0;
        public Form1()
        {
            InitializeComponent();
        }

        private void btnClickThis_Click(object sender, EventArgs e)
        {
           
        }

        private void lblHelloWorld_Click(object sender, EventArgs e)
        {

        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void buttonSave_Click(object sender, EventArgs e)
        {
            // saves items to respective lists. checks to make sure all entries are filled
            if (this.textBoxName.Text!= "" && this.textBoxQuantity.Text != "" && this.textBoxUnitPrice.Text != "")
            {
                ItemList.Items.Add(this.textBoxName.Text);
                this.textBoxName.Focus();
                this.textBoxName.Clear();

                double quantity = Convert.ToDouble(textBoxQuantity.Text);
                QuantityList.Items.Add(quantity);
                this.textBoxQuantity.Focus();
                this.textBoxQuantity.Clear();

             

                double price = Convert.ToDouble(textBoxUnitPrice.Text) * .06;
                
                PriceList.Items.Add(price);
                totalPrice += price;

                labelTotalCost.Text = totalPrice.ToString();

                this.textBoxUnitPrice.Focus();
                this.textBoxUnitPrice.Clear();
            }
            else
            {
                MessageBox.Show("Do not Leave Fields Empty", "Error", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }

            /*if (this.textBoxQuantity.Text != "")
            {
                ItemList.Items.Add(this.textBoxQuantity.Text);
                this.textBoxQuantity.Focus();
                this.textBoxQuantity.Clear();
            }
            else
            {
                MessageBox.Show("Enter Valid quantity.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }

            if (this.textBoxUnitPrice.Text != "")
            {
                ItemList.Items.Add(this.textBoxUnitPrice.Text);
                this.textBoxUnitPrice.Focus();
                this.textBoxUnitPrice.Clear();
            }
            else
            {
                MessageBox.Show("Enter Valid price.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }*/
        }

        private void ItemList_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void QuantityList_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void PriceList_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void Clear_Click(object sender, EventArgs e)
        {
            ItemList.Items.Clear();
            QuantityList.Items.Clear();
            PriceList.Items.Clear();
        }

        private void labelTotalCost_Click(object sender, EventArgs e)
        {

        }
    }
}
