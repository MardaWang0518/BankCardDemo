package com.card.mardawang.bankcarddemo;

import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.text.Html;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

//根据银行卡号获取银行及银行卡类型
public class MainActivity extends AppCompatActivity {
    private String extra= "知识扩展"+"<br/>"+"<font color='#333333'><big>Luhn</big></font> <font color='#999999'><small>检验数字算法（Luhn Check Digit Algorithm），也叫做模数10公式，是一种简单的算法，用于" +
            "验证银行卡、信用卡号码的有效性的算法。对所有大型信用卡公司发行的信用卡都起作用，这些公司包括美国Express、护照、" +
            "万事达卡、Discover和用餐者俱乐部等。这种算法最初是在20世纪60年代由一组数学家制定，现在Luhn检验数字算法属于大众，" +
            "任何人都可以使用它。<br/>" + "<br/>" +
            "算法：将每个奇数加倍和使它变为单个的数字，如果必要的话通过减去9和在每个偶数上加上这些值。如果此卡要有效，那么，结果必须是10的倍数。</small></font>";

    private EditText et_cardnum;
    private TextView tv_bankname;
    private TextView tv_cardtype;
    private TextView tv_extra;
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
        tv_extra = (TextView) findViewById(R.id.tv_extra);
        btn_get = (Button) findViewById(R.id.tv_get);

        tv_extra.setText(Html.fromHtml(extra));

        btn_get.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                cardnum = et_cardnum.getText().toString().trim();
                if (cardnum!=null && checkBankCard(cardnum)) {
                    bankinfobean = new BankInfoBean(cardnum);
                    tv_bankname.setText(bankinfobean.getBankName());
                    tv_cardtype.setText(bankinfobean.getCardType());
                } else {
                    Toast.makeText(MainActivity.this, "卡号 "+cardnum+" is NOT valid", Toast.LENGTH_SHORT).show();
                }
            }
        });

    }

    /**校验过程：
        1、从卡号最后一位数字开始，逆向将奇数位(1、3、5等等)相加。
        2、从卡号最后一位数字开始，逆向将偶数位数字，先乘以2（如果乘积为两位数，将个位十位数字相加，即将其减去9），再求和。
        3、将奇数位总和加上偶数位总和，结果应该可以被10整除。
     * 校验银行卡卡号
     */
    public static boolean checkBankCard(String bankCard) {
        if(bankCard.length() < 15 || bankCard.length() > 19) {
            return false;
        }
        char bit = getBankCardCheckCode(bankCard.substring(0, bankCard.length() - 1));
        if(bit == 'N'){
            return false;
        }
        return bankCard.charAt(bankCard.length() - 1) == bit;
    }

    /**
     * 从不含校验位的银行卡卡号采用 Luhn 校验算法获得校验位
     * @param nonCheckCodeBankCard
     * @return
     */
    public static char getBankCardCheckCode(String nonCheckCodeBankCard){
        if(nonCheckCodeBankCard == null || nonCheckCodeBankCard.trim().length() == 0
                || !nonCheckCodeBankCard.matches("\\d+")) {
            //如果传的不是数据返回N
            return 'N';
        }
        char[] chs = nonCheckCodeBankCard.trim().toCharArray();
        int luhmSum = 0;
        for(int i = chs.length - 1, j = 0; i >= 0; i--, j++) {
            int k = chs[i] - '0';
            if(j % 2 == 0) {
                k *= 2;
                k = k / 10 + k % 10;
            }
            luhmSum += k;
        }
        return (luhmSum % 10 == 0) ? '0' : (char)((10 - luhmSum % 10) + '0');
    }
}
