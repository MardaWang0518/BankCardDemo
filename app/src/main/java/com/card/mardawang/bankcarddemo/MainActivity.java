package com.card.mardawang.bankcarddemo;

import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

//根据银行卡号获取银行及银行卡类型
public class MainActivity extends AppCompatActivity {

    private EditText et_cardnum;
    private TextView tv_bankname;
    private TextView tv_cardtype;
    private String cardnum;
    private BankInfoBean bankinfobean;
    private Button btn_get;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        initView();
    }

    private void initView() {
        et_cardnum = (EditText) findViewById(R.id.et_cardnum);
        tv_bankname = (TextView) findViewById(R.id.tv_bankname);
        tv_cardtype = (TextView) findViewById(R.id.tv_cardtype);
        btn_get = (Button) findViewById(R.id.tv_get);


        btn_get.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                cardnum = et_cardnum.getText().toString().trim();
                if (cardnum!=null && cardnum.length()>6) {
                    bankinfobean = new BankInfoBean(cardnum);
                    tv_bankname.setText(bankinfobean.getBankName());
                    tv_cardtype.setText(bankinfobean.getCardType());
                } else {
                    Toast.makeText(MainActivity.this, "请输入正确银行卡号", Toast.LENGTH_SHORT).show();
                }
            }
        });

    }

}
