import java.awt.*;
import javax.swing.*;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.DocumentBuilder;
import org.w3c.dom.Document;
import org.w3c.dom.NodeList;
import org.w3c.dom.Element;
import java.io.File;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import javax.swing.JFrame;
import java.awt.Container;
import javax.swing.WindowConstants;
import java.awt.Color;
import java.awt.BorderLayout;
import java.awt.GridLayout;
import javax.swing.JButton;
import java.awt.FlowLayout;

public class BasicSmartGridGUI extends JFrame
{ 
    public static void main (String [] args){      
      try
      {//Step 1: Open the XML file
      File file=new File("/home/pi/Desktop/home.xml");
      
      DocumentBuilderFactory dbf=DocumentBuilderFactory.newInstance();
      
      DocumentBuilder db=dbf.newDocumentBuilder();
      
      Document document=db.parse(file);
      
      document.getDocumentElement().normalize();
     
      //Step 2: Create the GUI
      JFrame gui=new JFrame();
      gui.setTitle("Smart Grid Communications");
      gui.setResizable(false);
      gui.setSize(500,500);
      gui.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
      

      //Step 2: Create the grid that displays the data in the XML file
      Container pane = gui.getContentPane();
      pane.setLayout(new GridLayout(5,2,5,5)); 
      JLabel label1=new JLabel("Home ID");
      JLabel label11=new JLabel(document.getElementsByTagName("HomeID").item(0).getTextContent());
      JLabel label2=new JLabel("Customer ID");
      JLabel label22=new JLabel(document.getElementsByTagName("ClientID").item(0).getTextContent());
      JLabel label3=new JLabel("Current Consumption");
      JLabel label33=new JLabel(document.getElementsByTagName("CurrentConsumption").item(0).getTextContent());
      JLabel label4=new JLabel("Predicted Consumption");
      JLabel label44=new JLabel(document.getElementsByTagName("PredictedConsumption").item(0).getTextContent());
      JLabel label5=new JLabel("Green Energy Stored");
      JLabel label55=new JLabel(document.getElementsByTagName("GreenEnergyStored").item(0).getTextContent());
       
      pane.setComponentOrientation(ComponentOrientation.LEFT_TO_RIGHT);
      pane.add(label1);
      pane.add(label11);
      pane.add(label2);
      pane.add(label22);
      pane.add(label3);
      pane.add(label33);
      pane.add(label4);
      pane.add(label44);
      pane.add(label5);
      pane.add(label55);
              
      gui.setVisible(true);
      
      }
    
        catch(Exception ex)
        {
        System.out.println("Error reading XML file");
        System.out.println(ex.getMessage());
        }     
    }
}
