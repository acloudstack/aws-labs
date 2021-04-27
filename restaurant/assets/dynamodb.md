<table>
    <thead>
        <tr>
            <th colspan=2>Primary Key</th>
            <th rowspan=2 colspan=3>Attributes</th>
        </tr>
        <tr>
            <th>Partition Key</th>
            <th>Sort Key</th>
        </tr>
    </thead>
    <tbody>
        <!-- Start of CERTIFICATION#SAA-C02 -->
        <tr>
            <td rowspan=10>CERTIFICATION#SAA-C02#001</td> <!-- PK -->
            <td rowspan=2>DOMAIN#001</td>                 <!-- SK -->           
            <td>NAME</td>
            <td>TYPE</td>       
            <td>CATEGORY</td>   
            <td>LEVEL</td>      
            <td>DOMAIN</td> 
            <td>LSI_TYPE_DOMAIN</td> <!-- LSI -->    
            <td>LSI_TYPE_DOMAIN_LEVEL</td> <!-- LSI -->
            <td>LSI_TYPE_DOMAIN_CATEGORY</td> <!-- LSI -->
            <td>LSI_TYPE_DOMAIN_CATEGORY_LEVEL</td> <!-- LSI -->
            <td>LSI_TYPE_CATEGORY</td> <!-- LSI -->
        </tr>
        <tr>            
            <td>Design Resilient Architectures</td>
            <td>DOMAIN</td>
            <td>dummy category</td>
            <td>000</td>      
            <td>000</td> 
            <td>LSI_TYPE_DOMAIN</td> <!-- LSI -->    
            <td>LSI_TYPE_DOMAIN_LEVEL</td> <!-- LSI -->
            <td>LSI_TYPE_DOMAIN_CATEGORY</td> <!-- LSI -->
            <td>LSI_TYPE_DOMAIN_CATEGORY_LEVEL</td> <!-- LSI -->
            <td>LSI_TYPE_CATEGORY</td> <!-- LSI -->
        </tr>
        <tr>
            <td rowspan=2>DOMAIN#002</td>
            <td>NAME</td>
            <td>TYPE</td>
            <td>CATEGORY</td>
            <td>LEVEL</td>      
            <td>DOMAIN</td> 
            <td>LSI_TYPE_DOMAIN</td> <!-- LSI -->    
            <td>LSI_TYPE_DOMAIN_LEVEL</td> <!-- LSI -->
            <td>LSI_TYPE_DOMAIN_CATEGORY</td> <!-- LSI -->
            <td>LSI_TYPE_DOMAIN_CATEGORY_LEVEL</td> <!-- LSI -->
            <td>LSI_TYPE_CATEGORY</td> <!-- LSI -->
        </tr>
        <tr>
            <td>Design High-Performing Architectures</td>
            <td>DOMAIN</td>
            <td>dummy_category</td>
            <td>000</td>      
            <td>000</td> 
            <td>LSI_TYPE_DOMAIN</td> <!-- LSI -->    
            <td>LSI_TYPE_DOMAIN_LEVEL</td> <!-- LSI -->
            <td>LSI_TYPE_DOMAIN_CATEGORY</td> <!-- LSI -->
            <td>LSI_TYPE_DOMAIN_CATEGORY_LEVEL</td> <!-- LSI -->
            <td>LSI_TYPE_CATEGORY</td> <!-- LSI -->
        </tr>
        <tr>
            <td rowspan=2>DOMAIN#003</td>
            <td>NAME</td>
            <td>TYPE</td>
            <td>CATEGORY</td>
            <td>LEVEL</td>      
            <td>DOMAIN</td> 
            <td>LSI_TYPE_DOMAIN</td> <!-- LSI -->    
            <td>LSI_TYPE_DOMAIN_LEVEL</td> <!-- LSI -->
            <td>LSI_TYPE_DOMAIN_CATEGORY</td> <!-- LSI -->
            <td>LSI_TYPE_DOMAIN_CATEGORY_LEVEL</td> <!-- LSI -->
            <td>LSI_TYPE_CATEGORY</td> <!-- LSI -->
        </tr>
        <tr>
            <td>Design Secure Applications and Architectures</td>
            <td>DOMAIN</td>
            <td>category</td>
            <td>LEVEL</td>      
            <td>DOMAIN</td> 
            <td>LSI_TYPE_DOMAIN</td> <!-- LSI -->    
            <td>LSI_TYPE_DOMAIN_LEVEL</td> <!-- LSI -->
            <td>LSI_TYPE_DOMAIN_CATEGORY</td> <!-- LSI -->
            <td>LSI_TYPE_DOMAIN_CATEGORY_LEVEL</td> <!-- LSI -->
            <td>LSI_TYPE_CATEGORY</td> <!-- LSI -->
        </tr>
        <tr>
            <td rowspan=2>QUESTION#001</td>            
            <td>NAME</td>
            <td>TYPE</td>
            <td>CATEGORY</td>
            <td>LEVEL</td>      
            <td>DOMAIN</td> 
            <td>LSI_TYPE_DOMAIN</td> <!-- LSI -->    
            <td>LSI_TYPE_DOMAIN_LEVEL</td> <!-- LSI -->
            <td>LSI_TYPE_DOMAIN_CATEGORY</td> <!-- LSI -->
            <td>LSI_TYPE_DOMAIN_CATEGORY_LEVEL</td> <!-- LSI -->
            <td>LSI_TYPE_CATEGORY</td> <!-- LSI -->
        </tr>
        <tr>
            <td>json string for questions</td>
            <td>QUESTION</td>       <!-- type -->
            <td>C001</td>           <!-- category -->
            <td>L100</td>           <!-- level -->    
            <td>D001</td>           <!-- domain -->
            <td>QUESTION_D001</td>  <!-- lsi_type_domain -->    
            <td>QUESTION_D001_L001</td>     <!-- lsi_type_domain_level -->
            <td>QUESTION_D001_C001</td>     <!-- lsi_type_domain_category -->
            <td>QUESTION_D001_C001_100</td> <!-- lsi_type_domain_category_level -->
            <td>QUESTION_C001</td>          <!-- lsi_type_category -->
        </tr>
        <tr>
            <td rowspan=2>QUESTION#002</td>            
            <td>NAME</td>
            <td>TYPE</td>
            <td>CATEGORY</td>
            <td>LEVEL</td>      
            <td>DOMAIN</td> 
            <td>LSI_TYPE_DOMAIN</td> <!-- LSI -->    
            <td>LSI_TYPE_DOMAIN_LEVEL</td> <!-- LSI -->
            <td>LSI_TYPE_DOMAIN_CATEGORY</td> <!-- LSI -->
            <td>LSI_TYPE_DOMAIN_CATEGORY_LEVEL</td> <!-- LSI -->
            <td>LSI_TYPE_CATEGORY</td> <!-- LSI -->
        </tr>
        <tr>
            <td>NAME</td>
            <td>TYPE</td>
            <td>CATEGORY</td>
            <td>LEVEL</td>      
            <td>DOMAIN</td> 
            <td>LSI_TYPE_DOMAIN</td> <!-- LSI -->    
            <td>LSI_TYPE_DOMAIN_LEVEL</td> <!-- LSI -->
            <td>LSI_TYPE_DOMAIN_CATEGORY</td> <!-- LSI -->
            <td>LSI_TYPE_DOMAIN_CATEGORY_LEVEL</td> <!-- LSI -->
            <td>LSI_TYPE_CATEGORY</td> <!-- LSI -->
        </tr>
        <!-- End of CERTIFICATION#SAA-C02 -->
        <!-- Start of CERTIFICATION#SAP-C01 -->
        <tr>
            <td rowspan=4>CERTIFICATION#SAP-C01</td>
            <td rowspan=2>C2 Name A</td>
            <td>Attr1</td>
            <td>Attr2</td>
            <td>Attr3</td>
        </tr>
        <tr>
            <td>C3 Name B</td>
            <td>C3 Name B</td>
            <td>C3 Name B</td>
        </tr>
        <tr>
            <td rowspan=2>C2 Name B</td>
            <td>Attr1</td>
            <td>Attr2</td>
            <td>Attr3</td>
        </tr>
        <tr>
            <td>C3 Name D</td>
            <td>C3 Name D</td>
            <td>C3 Name D</td>
        </tr>
        <!-- End of CERTIFICATION#SAP-C01 -->
    </tbody>
</table>